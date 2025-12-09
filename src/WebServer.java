import static spark.Spark.*;
import java.util.*;
import org.json.*;
import java.nio.file.*;

public class WebServer {
    public static void main(String[] args) {
        // Диагностика
        System.out.println("\n" + "=".repeat(50));
        System.out.println("Starting WebServer...");
        System.out.println("Working Directory: " + System.getProperty("user.dir"));
        System.out.println("=".repeat(50) + "\n");
        
        port(8080);

        // Enable CORS
        options("/*", (request, response) -> {
            String accessControlRequestHeaders = request.headers("Access-Control-Request-Headers");
            if (accessControlRequestHeaders != null) {
                response.header("Access-Control-Allow-Headers", accessControlRequestHeaders);
            }
            String accessControlRequestMethod = request.headers("Access-Control-Request-Method");
            if (accessControlRequestMethod != null) {
                response.header("Access-Control-Allow-Methods", accessControlRequestMethod);
            }
            return "OK";
        });

        before((request, response) -> {
            response.header("Access-Control-Allow-Origin", "*");
            response.header("Access-Control-Request-Method", "GET,POST,PUT,DELETE,OPTIONS");
            response.header("Access-Control-Allow-Headers", "Content-Type,Authorization,X-Requested-With,Content-Length,Accept,Origin");
        });

        // 1. Получить все темы
        get("/topics", (req, res) -> {
            res.type("application/json");
            try {
                String topics = WebProblemLoader.getTopics();
                JSONObject responseJson = new JSONObject();
                responseJson.put("topics", topics.split(","));
                return responseJson.toString();
            } catch (Exception e) {
                res.status(500);
                return "{\"error\": \"" + e.getMessage() + "\"}";
            }
        });

        // 2. Получить задачи по теме
        get("/problems/:topic", (req, res) -> {
            res.type("application/json");
            try {
                String topic = req.params(":topic");
                String problems = WebProblemLoader.getProblemsByTopic(topic);
                JSONObject responseJson = new JSONObject();
                responseJson.put("problems", problems);
                return responseJson.toString();
            } catch (Exception e) {
                res.status(500);
                return "{\"error\": \"" + e.getMessage() + "\"}";
            }
        });

        // 3. Получить условие задачи
        get("/problem/:id", (req, res) -> {
            res.type("application/json");
            try {
                String id = req.params(":id");
                String problemInfo = WebProblemLoader.getProblemInfo(id);
                JSONObject responseJson = new JSONObject();
                responseJson.put("problem", problemInfo);
                return responseJson.toString();
            } catch (Exception e) {
                res.status(500);
                return "{\"error\": \"" + e.getMessage() + "\"}";
            }
        });

        // 4. Проверить решение
        post("/judge", (req, res) -> {
            res.type("application/json");
            try {
                JSONObject request = new JSONObject(req.body());
                String problemId = request.getString("problemId");
                String code = request.getString("code");
                
                String result = Judge.runAndTest(problemId, code);
                
                JSONObject responseJson = new JSONObject();
                responseJson.put("result", result);
                return responseJson.toString();
            } catch (Exception e) {
                res.status(500);
                JSONObject error = new JSONObject();
                error.put("error", e.getMessage());
                return error.toString();
            }
        });

        // 5. ПОЛУЧИТЬ ЭТАЛОННОЕ РЕШЕНИЕ - ДОБАВЬТЕ ЭТОТ МАРШРУТ!
        get("/solution/:id", (req, res) -> {
            System.out.println("\n=== SOLUTION REQUEST ===");
            System.out.println("Problem ID: " + req.params(":id"));
            
            res.type("application/json");
            try {
                String id = req.params(":id");
                
                // Используем базовый путь
                Path baseDir = Paths.get(System.getProperty("user.dir"));
                Path solutionPath = baseDir.resolve("problems").resolve(id).resolve("attempt.py");
                
                System.out.println("Solution path: " + solutionPath);
                System.out.println("File exists: " + Files.exists(solutionPath));
                
                if (Files.exists(solutionPath)) {
                    String solution = Files.readString(solutionPath);
                    JSONObject responseJson = new JSONObject();
                    responseJson.put("solution", solution);
                    responseJson.put("language", "python");
                    System.out.println("Solution sent successfully");
                    return responseJson.toString();
                } else {
                    System.out.println("ERROR: Solution file not found!");
                    res.status(404);
                    return "{\"error\": \"Решение не найдено для задачи " + id + "\"}";
                }
            } catch (Exception e) {
                System.err.println("ERROR in /solution: " + e.getMessage());
                e.printStackTrace();
                res.status(500);
                return "{\"error\": \"" + e.getMessage() + "\"}";
            }
        });

        // Health check
        get("/health", (req, res) -> "OK");

        // 404 handler
        notFound((req, res) -> {
            res.type("application/json");
            return "{\"error\": \"Route not found: " + req.pathInfo() + "\"}";
        });

        System.out.println("Judge Server started on http://localhost:8080");
        System.out.println("Available routes:");
        System.out.println("  GET  /topics");
        System.out.println("  GET  /problems/:topic");
        System.out.println("  GET  /problem/:id");
        System.out.println("  POST /judge");
        System.out.println("  GET  /solution/:id  <-- НОВЫЙ МАРШРУТ!");
        System.out.println("  GET  /health");
    }
}