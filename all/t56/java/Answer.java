import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Character> findShiftJisNotGbk() {
        /*
         * Find all the characters that can be represented in Shift-JIS, but not in GBK,
         * and return them as an array
         *
         * Returns:
         *     List<Character>: A list of characters that are unique to Shift-JIS, not encodable in GBK.
         */

        Charset shiftJis = Charset.forName("Shift_JIS");
        Charset gbk = Charset.forName("GBK");

        List<Character> result = new ArrayList<>();

        for (char c = 0; c < Character.MAX_VALUE; c++) {
            String str = String.valueOf(c);
            if (shiftJis.canEncode(str) && !gbk.canEncode(str)) {
                result.add(c);
            }
        }

        return result;
    }
}
