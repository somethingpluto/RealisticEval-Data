public class Answer {
    public static List<String> splitString(String str) {
        List<String> result = new ArrayList<>();
        String[] words = str.trim().split("\\s+");

        for (String word : words) {
            if (!word.isEmpty()) {
                result.add(word);
            }
        }

        return result;
    }
}