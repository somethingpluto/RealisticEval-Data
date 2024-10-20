package org.real.temp;

import java.util.HashMap;
import java.util.Map;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Answer {

    private static final String DEFAULT_CONTEXT = "https://schema.lab.fiware.org/ld/context";
    private static final String UNKNOWN_ID = "urn:ngsi-ld:unknown:id";
    private static final String UNKNOWN_TYPE = "UnknownType";

    /**
     * Convert RDF JSON-LD question to NGSI-LD format.
     *
     * @param rdfJsonLd RDF JSON-LD formatted question as a string or map.
     * @return Data formatted according to NGSI-LD specifications.
     */
    public Map<String, Object> rdfJsonldToNgSILD(Object rdfJsonLd) {
        ObjectMapper objectMapper = new ObjectMapper();
        Map<String, Object> ngsiLd = new HashMap<>();

        try {
            if (rdfJsonLd instanceof String) {
                JsonNode jsonNode = objectMapper.readTree((String) rdfJsonLd);
                rdfJsonLd = objectMapper.convertValue(jsonNode, Map.class);
            }

            Map<String, Object> rdfJsonLdMap = (Map<String, Object>) rdfJsonLd;

            ngsiLd.put("id", rdfJsonLdMap.getOrDefault("@id", UNKNOWN_ID));
            ngsiLd.put("type", rdfJsonLdMap.getOrDefault("@type", UNKNOWN_TYPE));
            ngsiLd.put("@context", rdfJsonLdMap.getOrDefault("@context", DEFAULT_CONTEXT));
            ngsiLd.put("attributes", new ArrayList<>());

            // Assuming simple attribute structure conversion
            for (Map.Entry<String, Object> entry : rdfJsonLdMap.entrySet()) {
                String key = entry.getKey();
                Object value = entry.getValue();
                if (!key.equals("@context") && !key.equals("@id") && !key.equals("@type")) {
                    Map<String, Object> attribute = new HashMap<>();
                    attribute.put("type", "Property");
                    attribute.put("name", key);
                    attribute.put("value", value);
                    ((List<Map<String, Object>>) ngsiLd.get("attributes")).add(attribute);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return ngsiLd;
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        // Example usage
        String rdfJsonLdStr = "{\"@id\": \"urn:ngsi-ld:example\", \"@type\": \"ExampleType\", \"attr1\": \"value1\", \"attr2\": 42}";
        Map<String, Object> result = answer.rdfJsonldToNgSILD(rdfJsonLdStr);
        System.out.println(result);
    }
}