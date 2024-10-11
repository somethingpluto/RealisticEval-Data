import static org.junit.Assert.assertEquals;
import org.json.JSONObject;
import org.junit.Test;

public class Tester {

    @Test
    public void testRDFJSONLDToNGSILD() throws Exception {
        // Arrange
        String rdfJsonLd = "{\"@context\": \"http://example.com\", \"name\": \"John\"}";

        // Act
        JSONObject ngsiLdResult = rdfJsonLdToNgSILDRdfJsonLd(rdfJsonLd);

        // Assert
        assertEquals("John", ngsiLdResult.getString("name"));
    }

    private JSONObject rdfJsonLdToNgSILDRdfJsonLd(String rdfJsonLd) {
        // Implement the conversion logic here and return a JSONObject
        // This is just a placeholder for demonstration purposes
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("name", "John");
        return jsonObject;
    }
}