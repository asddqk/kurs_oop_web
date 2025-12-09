import java.io.*;
import java.nio.file.*;
import java.util.*;
import org.json.*;

public class WebProblemLoader {
    private static Path getBaseDir() {
        // Определяем корневую директорию проекта
        Path current = Paths.get("").toAbsolutePath();
        
        // Ищем папку problems (максимум 3 уровня вверх)
        for (int i = 0; i < 3; i++) {
            if (Files.exists(current.resolve("problems"))) {
                return current;
            }
            if (current.getParent() == null) break;
            current = current.getParent();
        }
        
        // Если не нашли, используем текущую
        return Paths.get(System.getProperty("user.dir"));
    }

    public static List<JSONObject> loadProblems() throws IOException {
        Path baseDir = getBaseDir();
        Path problemsDir = baseDir.resolve("problems");
        
        System.out.println("[WebProblemLoader] Loading from: " + problemsDir);
        
        List<JSONObject> problems = new ArrayList<>();
        File[] subdirs = problemsDir.toFile().listFiles(File::isDirectory);
        if (subdirs == null) return problems;

        for (File d : subdirs) {
            Path metaPath = d.toPath().resolve("meta.json");
            if (!Files.exists(metaPath)) continue;
            String content = Files.readString(metaPath);
            JSONObject j = new JSONObject(content);
            problems.add(j);
        }
        return problems;
    }

    public static String getProblemInfo(String id) throws IOException {
        Path baseDir = getBaseDir();
        Path folder = baseDir.resolve("problems").resolve(id);
        
        StringBuilder info = new StringBuilder();
        
        // Условие
        info.append("=== УСЛОВИЕ ===\n\n");
        info.append(Files.readString(folder.resolve("condition.txt")));
        
        // Пример ввода/вывода
        info.append("\n\n=== ПРИМЕР ===\n");
        info.append("Ввод:\n");
        info.append(Files.readString(folder.resolve("input.txt")));
        info.append("\nВывод:\n");
        info.append(Files.readString(folder.resolve("output.txt")));
        
        // Эталонное решение (если есть)
        Path attemptPath = folder.resolve("attempt.py");
        if (Files.exists(attemptPath)) {
            info.append("\n\n=== ЭТАЛОННОЕ РЕШЕНИЕ (Python) ===\n");
            info.append(Files.readString(attemptPath));
        }
        
        return info.toString();
    }

    public static String getTopics() throws IOException {
        List<JSONObject> problems = loadProblems();
        Set<String> topics = new HashSet<>();
        for (JSONObject p : problems) {
            topics.add(p.getString("topic"));
        }
        return String.join(",", topics);
    }

    public static String getProblemsByTopic(String topic) throws IOException {
        List<JSONObject> problems = loadProblems();
        StringBuilder result = new StringBuilder();
        
        for (JSONObject p : problems) {
            if (p.getString("topic").equalsIgnoreCase(topic)) {
                result.append(p.getString("id"))
                      .append(" - ")
                      .append(p.getString("name"))
                      .append(" (Сложность: ")
                      .append(p.getInt("difficulty"))
                      .append("%)\n");
            }
        }
        
        return result.toString();
    }
}