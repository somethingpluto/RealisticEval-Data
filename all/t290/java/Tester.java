package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Tester {

    private static final String DEFAULT_CONTEXT = "https://schema.lab.fiware.org/ld/context";
    private static final String UNKNOWN_ID = "urn:ngsi-ld:unknown:id";
    private static final String UNKNOWN_TYPE = "UnknownType";

    private static final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Converts the question in RDF JSON-LD format to NGSI-LD format.
     *
     * @param rdfJsonLd The RDF JSON-LD formatted question as a string.
     * @return A map containing data formatted according to NGSI-LD specifications.
     */
    public Map<String, Object> rdfJsonldToNgSILD(String rdfJsonLd) {
        try {
            if (rdfJsonLd == null || rdfJsonLd.trim().isEmpty()) {
                throw new IllegalArgumentException("Invalid JSON input");
            }

            JsonNode jsonNode = objectMapper.readTree(rdfJsonLd);
            Map<String, Object> rdfJsonLdMap = objectMapper.convertValue(jsonNode, Map.class);

            Map<String, Object> ngsiLd = new HashMap<>();
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

            return ngsiLd;
        } catch (JsonProcessingException e) {
            throw new IllegalArgumentException("Invalid JSON input", e);
        }
    }

    @Test
    public void testBasicConversion() throws JsonProcessingException {
        String rdfJsonld = objectMapper.writeValueAsString(new HashMap<String, Object>() {{
            put("@context", "http://schema.org/");
            put("@id", "urn:ngsi-ld:Vehicle:A123");
            put("@type", "Vehicle");
            put("speed", new HashMap<String, Object>() {{
                put("value", 60);
                put("unitCode", "KMH");
            }});
        }});

        Map<String, Object> expectedNgsild = new HashMap<>();
        expectedNgsild.put("id", "urn:ngsi-ld:Vehicle:A123");
        expectedNgsild.put("type", "Vehicle");
        expectedNgsild.put("@context", "http://schema.org/");
        expectedNgsild.put("attributes", new ArrayList<Map<String, Object>>() {{
            add(new HashMap<String, Object>() {{
                put("type", "Property");
                put("name", "speed");
                put("value", new HashMap<String, Object>() {{
                    put("value", 60);
                    put("unitCode", "KMH");
                }});
            }});
        }});

        Map<String, Object> result = rdfJsonldToNgSILD(rdfJsonld);
        assertEquals(expectedNgsild, result);
    }

    @Test
    public void testMissingIdAndType() throws JsonProcessingException {
        String rdfJsonld = objectMapper.writeValueAsString(new HashMap<String, Object>() {{
            put("@context", "http://schema.org/");
            put("speed", new HashMap<String, Object>() {{
                put("value", 60);
                put("unitCode", "KMH");
            }});
        }});

        Map<String, Object> expectedNgsild = new HashMap<>();
        expectedNgsild.put("id", UNKNOWN_ID);
        expectedNgsild.put("type", UNKNOWN_TYPE);
        expectedNgsild.put("@context", "http://schema.org/");
        expectedNgsild.put("attributes", new ArrayList<Map<String, Object>>() {{
            add(new HashMap<String, Object>() {{
                put("type", "Property");
                put("name", "speed");
                put("value", new HashMap<String, Object>() {{
                    put("value", 60);
                    put("unitCode", "KMH");
                }});
            }});
        }});

        Map<String, Object> result = rdfJsonldToNgSILD(rdfJsonld);
        assertEquals(expectedNgsild, result);
    }

    @Test
    public void testWithNestedObjects() throws JsonProcessingException {
        String rdfJsonld = objectMapper.writeValueAsString(new HashMap<String, Object>() {{
            put("@context", "http://schema.org/");
            put("@id", "urn:ngsi-ld:Vehicle:A123");
            put("@type", "Vehicle");
            put("location", new HashMap<String, Object>() {{
                put("latitude", 48.8566);
                put("longitude", 2.3522);
            }});
        }});

        Map<String, Object> expectedNgsild = new HashMap<>();
        expectedNgsild.put("id", "urn:ngsi-ld:Vehicle:A123");
        expectedNgsild.put("type", "Vehicle");
        expectedNgsild.put("@context", "http://schema.org/");
        expectedNgsild.put("attributes", new ArrayList<Map<String, Object>>() {{
            add(new HashMap<String, Object>() {{
                put("type", "Property");
                put("name", "location");
                put("value", new HashMap<String, Object>() {{
                    put("latitude", 48.8566);
                    put("longitude", 2.3522);
                }});
            }});
        }});

        Map<String, Object> result = rdfJsonldToNgSILD(rdfJsonld);
        assertEquals(expectedNgsild, result);
    }

    @Test
    public void testInvalidJsonInput() {
        String rdfJsonld = "This is not a valid JSON";
        assertThrows(IllegalArgumentException.class, () -> rdfJsonldToNgSILD(rdfJsonld));
    }

    @Test
    public void testEmptyJsonld() throws JsonProcessingException {
        String rdfJsonld = objectMapper.writeValueAsString(new HashMap<>());

        Map<String, Object> expectedNgsild = new HashMap<>();
        expectedNgsild.put("id", UNKNOWN_ID);
        expectedNgsild.put("type", UNKNOWN_TYPE);
        expectedNgsild.put("@context", DEFAULT_CONTEXT);
        expectedNgsild.put("attributes", new ArrayList<>());

        Map<String, Object> result = rdfJsonldToNgSILD(rdfJsonld);
        assertEquals(expectedNgsild, result);
    }
}
