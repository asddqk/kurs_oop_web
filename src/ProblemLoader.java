import java.io.*;
import java.nio.file.*;
import java.util.*;
import org.json.*;

public class ProblemLoader {

    public static List<JSONObject> loadProblems(String folder) throws IOException {
        List<JSONObject> problems = new ArrayList<>();
        File dir = new File(folder);
        File[] subdirs = dir.listFiles(File::isDirectory);
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

    public static void showProblem(String id) throws IOException {
        Path folder = Path.of("problems", id);

        System.out.println("Условие");
        System.out.println(Files.readString(folder.resolve("condition.txt")));

        System.out.println("\nПример ввода");
        System.out.println(Files.readString(folder.resolve("input.txt")));

        System.out.println("\nПример вывода");
        System.out.println(Files.readString(folder.resolve("output.txt")));
    }
}
