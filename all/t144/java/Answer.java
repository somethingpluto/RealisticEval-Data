import java.util.HashMap;
import java.util.Map;

public class NumberConverter {
    public static String arabicToEnglishNumbers(String value) {
        Map<Character, Character> arabicToEnglishMap = new HashMap<>();
        arabicToEnglishMap.put('٠', '0');
        arabicToEnglishMap.put('١', '1');
        arabicToEnglishMap.put('٢', '2');
        arabicToEnglishMap.put('٣', '3');
        arabicToEnglishMap.put('٤', '4');
        arabicToEnglishMap.put('٥', '5');
        arabicToEnglishMap.put('٦', '6');
        arabicToEnglishMap.put('٧', '7');
        arabicToEnglishMap.put('٨', '8');
        arabicToEnglishMap.put('٩', '9');

        StringBuilder result = new StringBuilder();
        for (char ch : value.toCharArray()) {
            result.append(arabicToEnglishMap.getOrDefault(ch, ch));
        }
        return result.toString();
    }
}