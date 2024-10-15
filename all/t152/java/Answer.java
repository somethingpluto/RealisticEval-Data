import java.util.HashMap;
import java.util.Map;

public class MathSansSerifItalicConverter {

    public static String convertToMathematicalSansSerifItalic(String input) {
        Map<Character, String> characterMap = new HashMap<>();
        characterMap.put('A', "𝑨"); characterMap.put('B', "𝑩"); characterMap.put('C', "𝑪");
        characterMap.put('D', "𝑫"); characterMap.put('E', "𝑬"); characterMap.put('F', "𝑭");
        characterMap.put('G', "𝑮"); characterMap.put('H', "𝑯"); characterMap.put('I', "𝑰");
        characterMap.put('J', "𝑱"); characterMap.put('K', "𝑲"); characterMap.put('L', "𝑳");
        characterMap.put('M', "𝑴"); characterMap.put('N', "𝑵"); characterMap.put('O', "𝑶");
        characterMap.put('P', "𝑷"); characterMap.put('Q', "𝑸"); characterMap.put('R', "𝑹");
        characterMap.put('S', "𝑺"); characterMap.put('T', "𝑻"); characterMap.put('U', "𝑼");
        characterMap.put('V', "𝑽"); characterMap.put('W', "𝑾"); characterMap.put('X', "𝑿");
        characterMap.put('Y', "𝒀"); characterMap.put('Z', "𝒁");
        characterMap.put('a', "𝒂"); characterMap.put('b', "𝒃"); characterMap.put('c', "𝒄");
        characterMap.put('d', "𝒅"); characterMap.put('e', "𝒆"); characterMap.put('f', "𝒇");
        characterMap.put('g', "𝒈"); characterMap.put('h', "𝒉"); characterMap.put('i', "𝒊");
        characterMap.put('j', "𝒋"); characterMap.put('k', "𝒌"); characterMap.put('l', "𝒍");
        characterMap.put('m', "𝒎"); characterMap.put('n', "𝒏"); characterMap.put('o', "𝒐");
        characterMap.put('p', "𝒑"); characterMap.put('q', "𝒒"); characterMap.put('r', "𝒓");
        characterMap.put('s', "𝒔"); characterMap.put('t', "𝒕"); characterMap.put('u', "𝒖");
        characterMap.put('v', "𝒗"); characterMap.put('w', "𝒘"); characterMap.put('x', "𝒙");
        characterMap.put('y', "𝒚"); characterMap.put('z', "𝒛");
        characterMap.put('0', "𝟢"); characterMap.put('1', "𝟣"); characterMap.put('2', "𝟤");
        characterMap.put('3', "𝟥"); characterMap.put('4', "𝟦"); characterMap.put('5', "𝟧");
        characterMap.put('6', "𝟨"); characterMap.put('7', "𝟩"); characterMap.put('8', "𝟪");
        characterMap.put('9', "𝟫");

        StringBuilder result = new StringBuilder();
        for (char c : input.toCharArray()) {
            result.append(characterMap.getOrDefault(c, String.valueOf(c)));
        }
        return result.toString();
    }
}