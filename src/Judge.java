import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class Judge {
    
    private static Path getBaseDir() {
        Path current = Paths.get("").toAbsolutePath();
        
        System.out.println("[Judge.getBaseDir] Starting from: " + current);
        
        for (int i = 0; i < 5; i++) {
            Path testProblems = current.resolve("problems");
            Path testSandbox = current.resolve("sandbox");
            
            System.out.println("[Judge.getBaseDir] Checking problems: " + testProblems);
            System.out.println("[Judge.getBaseDir] Problems exists: " + Files.exists(testProblems));
            System.out.println("[Judge.getBaseDir] Sandbox exists: " + Files.exists(testSandbox));
            
            if (Files.exists(testProblems) && Files.exists(testSandbox)) {
                System.out.println("[Judge.getBaseDir] Found base dir: " + current);
                return current;
            }
            
            if (current.getParent() == null) break;
            current = current.getParent();
        }
        
        Path fallback = Paths.get(System.getProperty("user.dir"));
        System.out.println("[Judge.getBaseDir] Using fallback: " + fallback);
        return fallback;
    }
    
    public static String runAndTest(String id, String userCode) throws IOException, InterruptedException {
        System.out.println("\n=== JUDGE START ===");
        System.out.println("[Judge] Problem ID: " + id);
        System.out.println("[Judge] Code length: " + userCode.length());
        
        Path baseDir = getBaseDir();
        
        // Создаём sandbox если не существует
        Path sandboxRoot = baseDir.resolve("sandbox");
        if (!Files.exists(sandboxRoot)) {
            System.out.println("[Judge] Creating sandbox root: " + sandboxRoot);
            Files.createDirectories(sandboxRoot);
        }
        
        // Проверяем тесты
        Path testFolder = baseDir.resolve("problems").resolve(id).resolve("test");
        System.out.println("[Judge] Test folder: " + testFolder);
        System.out.println("[Judge] Test folder exists: " + Files.exists(testFolder));
        
        if (!Files.exists(testFolder)) {
            return "❌ Ошибка: папка с тестами не найдена.\n" +
                   "Путь: " + testFolder + "\n" +
                   "Проверьте, что задача " + id + " существует.";
        }
        
        List<String[]> tests = new ArrayList<>();

        try (DirectoryStream<Path> stream = Files.newDirectoryStream(testFolder, "tin_*.txt")) {
            for (Path tin : stream) {
                String num = tin.getFileName().toString().replaceAll("\\D+", "");
                Path tout = testFolder.resolve("tout_" + num + ".txt");
                if (Files.exists(tout)) {
                    tests.add(new String[]{Files.readString(tin).trim(), Files.readString(tout).trim()});
                }
            }
        }

        if (tests.isEmpty()) {
            return "Ошибка: тесты не найдены для задачи " + id;
        }
        
        System.out.println("[Judge] Found " + tests.size() + " test(s)");

        StringBuilder result = new StringBuilder();
        boolean allPassed = true;

        for (int tIndex = 0; tIndex < tests.size(); tIndex++) {
            String[] test = tests.get(tIndex);
            int testNum = tIndex + 1;
            
            // Создаём уникальную папку для каждого теста
            String runId = "web_" + System.currentTimeMillis() + "_" + testNum + "_" + Thread.currentThread().getId();
            Path sandboxDir = sandboxRoot.resolve(runId);
            
            System.out.println("[Judge] Test #" + testNum + " sandbox: " + sandboxDir);
            
            if (Files.exists(sandboxDir)) {
                deleteDirectory(sandboxDir);
            }
            Files.createDirectories(sandboxDir);

            try {
                // Сохраняем код пользователя
                Path javaFile = sandboxDir.resolve("Main.java");
                Files.writeString(javaFile, userCode);

                // Создаём входной файл
                Path inputFile = sandboxDir.resolve("INPUT.TXT");
                Files.writeString(inputFile, test[0]);

                // КОМПИЛЯЦИЯ
                System.out.println("[Judge] Compiling test #" + testNum);
                ProcessBuilder compileBuilder = new ProcessBuilder("javac", "Main.java")
                        .directory(sandboxDir.toFile())
                        .redirectErrorStream(true);
                        
                Process compile = compileBuilder.start();
                
                // Читаем вывод компиляции
                StringBuilder compileOutput = new StringBuilder();
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(compile.getInputStream()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        compileOutput.append(line).append("\n");
                    }
                }
                
                int cRes = compile.waitFor();
                if (cRes != 0) {
                    result.append("❌ Ошибка компиляции для теста #").append(testNum).append("\n");
                    result.append(compileOutput.toString());
                    allPassed = false;
                    continue;
                }

                // ЗАПУСК
                System.out.println("[Judge] Running test #" + testNum);
                ProcessBuilder runBuilder = new ProcessBuilder("java", "Main")
                        .directory(sandboxDir.toFile())
                        .redirectErrorStream(true);
                        
                Process run = runBuilder.start();
                
                // Таймаут 2 секунды
                boolean finished = run.waitFor(2, TimeUnit.SECONDS);
                if (!finished) {
                    run.destroyForcibly();
                    result.append("❌ Превышено время выполнения теста #").append(testNum).append(" (2 секунды)\n");
                    allPassed = false;
                    continue;
                }

                // Чтение вывода программы
                StringBuilder outputBuilder = new StringBuilder();
                try (BufferedReader r = new BufferedReader(new InputStreamReader(run.getInputStream()))) {
                    String line;
                    while ((line = r.readLine()) != null) {
                        outputBuilder.append(line).append("\n");
                    }
                }
                
                String output = outputBuilder.toString().trim();
                String expected = test[1].trim();

                // Проверяем наличие OUTPUT.TXT
                Path outputFile = sandboxDir.resolve("OUTPUT.TXT");
                if (Files.exists(outputFile)) {
                    String fileOutput = Files.readString(outputFile).trim();
                    if (!fileOutput.isEmpty()) {
                        output = fileOutput; // Приоритет у OUTPUT.TXT
                    }
                }

                if (output.equals(expected)) {
                    result.append("✅ Тест #").append(testNum).append(": Пройден\n");
                } else {
                    result.append("❌ Тест #").append(testNum).append(": Ошибка\n");
                    result.append("Ожидалось:\n").append(expected).append("\n");
                    result.append("Получено:\n").append(output).append("\n");
                    allPassed = false;
                }
                
            } finally {
                // Очищаем папку теста
                try {
                    deleteDirectory(sandboxDir);
                } catch (IOException e) {
                    System.err.println("[Judge] Warning: could not delete sandbox " + sandboxDir + ": " + e.getMessage());
                }
            }
        }

        if (allPassed) {
            result.append("\n🎉 Все тесты пройдены! Задача решена верно!");
        } else {
            result.append("\n⚠️ Есть ошибки! Проверьте решение.");
        }
        
        System.out.println("[Judge] Result: " + (allPassed ? "PASSED" : "FAILED"));
        System.out.println("=== JUDGE END ===\n");
        
        return result.toString();
    }

    private static void deleteDirectory(Path path) throws IOException {
        if (Files.isDirectory(path)) {
            try (DirectoryStream<Path> entries = Files.newDirectoryStream(path)) {
                for (Path entry : entries) {
                    deleteDirectory(entry);
                }
            }
        }
        Files.deleteIfExists(path);
    }
}