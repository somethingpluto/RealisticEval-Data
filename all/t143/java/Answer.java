import java.util.HashMap;
import java.util.Map;

public class NumberConverter {
    public static String arabicToEnglishNumbers(String str) {
        Map<String, String> arabicNums = new HashMap<>();
        arabicNums.put("٠", "0");
        arabicNums.put("١", "1");
        arabicNums.put("٢", "2");
        arabicNums.put("٣", "3");
        arabicNums.put("٤", "4");
        arabicNums.put("٥", "5");
        arabicNums.put("٦", "6");
        arabicNums.put("٧", "7");
        arabicNums.put("٨", "8");
        arabicNums.put("٩", "9");

        StringBuilder result = new StringBuilder();
        for (char charAt : str.toCharArray()) {
            String charStr = String.valueOf(charAt);
            result.append(arabicNums.getOrDefault(charStr, charStr));
        }

        return result.toString();
    }
}