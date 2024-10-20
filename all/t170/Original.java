import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.nodes.Node;
import org.jsoup.nodes.TextNode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


class HtmlToMarkdownConverter {

    private static final Logger LOG = LoggerFactory.getLogger(HtmlToMarkdownConverter.class);

    private final int indentSize = 4;

    private int indent;

    private StringBuilder sb = new StringBuilder();

    public String convert(String html) {
        if (html != null) {
            Document doc = Jsoup.parseBodyFragment(html);
            convertElement(doc.body());
        }
        return sb.toString();
    }

    private void convertNode(Node node) {
        if (node instanceof TextNode) {
            TextNode textNode = (TextNode) node;
            sb.append(textNode.text());
        } else if (node instanceof Element) {
            Element element = (Element) node;
            convertElement(element);
        } else {
            throw new UnsupportedOperationException("Unknown node type " + node.getClass());
        }
    }

    private void convertChildren(Node node) {
        for (Node child : node.childNodes()) {
            convertNode(child);
        }
    }

    private void convertElement(Element element) {
        String tagName = element.tagName().toLowerCase();
        switch (tagName) {
            case "a":
                sb.append("[");
                convertChildren(element);
                sb.append("](");
                sb.append(element.attr("href"));
                sb.append(")");
                break;

            case "em":
            case "strong":
                sb.append("**");
                sb.append(element.html().replaceAll("\\s+", "**"));
                sb.append("**");
                break;

            case "code":
                sb.append("`");
                convertChildren(element);
                sb.append("`");
                break;

            case "pre":
                sb.append("```\n");
                sb.append(element.html());
                sb.append("\n```\n");
                break;

            case "p":
                convertChildren(element);
                sb.append("\n\n");
                break;

            case "br":
                sb.append("\n");
                break;

            case "u":
                sb.append("_");
                sb.append(element.html().replaceAll("\\s+", "_"));
                sb.append("_");
                break;

            case "ul":
                for (Element li : element.children()) {
                    sb.append("- ");
                    convertChildren(li);
                    sb.append("\n");
                }
                sb.append("\n");
                break;

            case "ol":
                int i = 1;
                for (Element li : element.children()) {
                    sb.append(i++);
                    sb.append(". ");
                    convertChildren(li);
                    sb.append("\n");
                }
                sb.append("\n");
                break;

            case "li":
                throw new UnsupportedOperationException("Bug: li should be handled by ul or ol");

            case "#root":
            case "html":
            case "body":
                convertChildren(element);
                break;

            default:
                // ignore tags we do not know
                LOG.warn("Unknown tag {}", tagName);
                convertChildren(element);
                break;
        }
    }
}