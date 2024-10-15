public class HTMLCompressor {

    public static String compressHTML(String html) {
        // Remove leading/trailing whitespace around tags
        html = html.replaceAll("\\s*(<[^>]+>)\\s*", "$1");
        // Remove multiple newlines and replace with a single space
        html = html.replaceAll("\\n+", " ");
        // Remove multiple spaces and replace them with a single space
        html = html.replaceAll("[ \\t]+", " ");
        return html.trim();
    }

    public static void main(String[] args) {
        String html = "   <div>   \n\n   Hello,   World!   \n\n   </div>   ";
        String compressedHTML = compressHTML(html);
        System.out.println(compressedHTML);
    }
}