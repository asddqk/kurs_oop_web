import java.nio.file.*;
import java.io.*;
import java.util.*;
import org.json.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        while (true) {
            List<JSONObject> problems = ProblemLoader.loadProblems("problems");

            // Получаем список уникальных тем
            Set<String> topics = new HashSet<>();
            for (JSONObject p : problems) topics.add(p.getString("topic"));

            System.out.println("Выберите тему (или 0 для выхода):");
            int tIndex = 1;
            List<String> topicList = new ArrayList<>(topics);
            for (String t : topicList) System.out.println(tIndex++ + ". " + t);
            System.out.print("Ваш выбор: ");
            int choice = sc.nextInt();
            sc.nextLine();

            if (choice == 0) {
                System.out.println("Выход...");
                break;
            }

            if (choice < 1 || choice > topicList.size()) {
                System.out.println("Неверный выбор. Попробуйте снова.\n");
                continue;
            }

            String selectedTopic = topicList.get(choice - 1);
            System.out.println("\nЗадачи по теме " + selectedTopic + ":\n");

            List<JSONObject> topicProblems = new ArrayList<>();
            for (JSONObject p : problems) {
                if (p.getString("topic").equalsIgnoreCase(selectedTopic)) {
                    System.out.println(p.getString("id") + " - " + p.getString("name") +
                            " (Сложность: " + p.getInt("difficulty") + "%)");
                    topicProblems.add(p);
                }
            }

            System.out.print("\nВведите ID задачи (например 1 для 0001): ");
            String idInput = sc.nextLine().trim();
            String id = String.format("%04d", Integer.parseInt(idInput)); // дополняем до 4 цифр

            // Очистка консоли (Windows)
            try {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } catch (Exception e) {
                // Игнорируем ошибки на других ОС
            }

            // Показ задачи
            ProblemLoader.showProblem(id);

            // Подготовка пользовательского решения
            System.out.println("\nСохраните решение в файл sub.txt, затем нажмите Enter...");
            sc.nextLine();

            // Очистка песочницы перед запуском
            Path sandbox = Path.of("sandbox");
            if (Files.exists(sandbox)) deleteDirectory(sandbox);

            // Запуск проверки
            //Judge.runAndTest(id);
            // Нужно передать код пользователя, но в консольной версии мы читаем из файла
// Для веб-версии это не нужно, но оставим для совместимости
            Path userFile = Path.of("sub.txt");
            if (Files.exists(userFile)) {
                String userCode = Files.readString(userFile);
                Judge.runAndTest(id, userCode);
            } else {
                System.out.println("Файл sub.txt не найден!");
            }
            // Показ примера решения (если есть)
            Path attempt = Path.of("problems", id, "attempt.py");
            if (Files.exists(attempt)) {
                System.out.println("\nПример решения (attempt.py):");
                System.out.println(Files.readString(attempt));
            }

            System.out.println("\nХотите решить ещё одну задачу? (y/n): ");
            String again = sc.nextLine().trim();
            if (!again.equalsIgnoreCase("y")) break;

            // Очистка консоли перед новым циклом
            try {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } catch (Exception e) {}
        }

        sc.close();
        System.out.println("Программа завершена.");
    }

    // Рекурсивное удаление папки
    private static void deleteDirectory(Path path) throws IOException {
        if (Files.isDirectory(path)) {
            try (DirectoryStream<Path> entries = Files.newDirectoryStream(path)) {
                for (Path entry : entries) deleteDirectory(entry);
            }
        }
        Files.delete(path);
    }
}
