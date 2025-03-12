from typing import Dict
import json

def rdf_jsonld_to_ngsild(rdf_jsonld: str) -> Dict:
    """
    Convert the question in RDF JSON-LD format to NGSI-LD format.

    Args:
        rdf_jsonld (str): RDF JSON-LD formatted question as a string.

    Returns:
        Data formatted according to NGSI-LD specifications.
    """
    # Parse the RDF JSON-LD string into a Python dictionary
    rdf_data = json.loads(rdf_jsonld)
    
    # Initialize an empty dictionary for the NGSI-LD format
    ngsi_ld_data = {}
    
    # Convert the RDF JSON-LD to NGSI-LD format
    for key, value in rdf_data.items():
        if key == "@context":
            # Convert the context to NGSI-LD context
            ngsi_ld_data["@context"] = value
        elif key == "@graph":
            # Process the graph data
            ngsi_ld_data["entities"] = []
            for entity in value:
                ngsi_ld_entity = {
                    "id": entity.get("@id", ""),
                    "type": entity.get("@type", ""),
                    "properties": {}
                }
                for prop_key, prop_value in entity.items():
                    if prop_key not in ["@id", "@type"]:
                        ngsi_ld_entity["properties"][prop_key] = prop_value
                ngsi_ld_data["entities"].append(ngsi_ld_entity)
        else:
            # Directly map other keys
            ngsi_ld_data[key] = value
    
    return ngsi_ld_data
import unittest
import json


class TestRDFJSONLDToNGSILDConversion(unittest.TestCase):
    def test_basic_conversion(self):
        """Test a basic and correct conversion from JSON-LD to NGSI-LD."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "@id": "urn:ngsi-ld:Vehicle:A123",
            "@type": "Vehicle",
            "speed": {"value": 60, "unitCode": "KMH"}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:Vehicle:A123",
            "type": "Vehicle",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "speed", "value": {"value": 60, "unitCode": "KMH"}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_missing_id_and_type(self):
        """Test conversion when @id and @type are missing."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "speed": {"value": 60, "unitCode": "KMH"}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:unknown:id",
            "type": "UnknownType",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "speed", "value": {"value": 60, "unitCode": "KMH"}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_with_nested_objects(self):
        """Test conversion with nested objects."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "@id": "urn:ngsi-ld:Vehicle:A123",
            "@type": "Vehicle",
            "location": {"latitude": 48.8566, "longitude": 2.3522}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:Vehicle:A123",
            "type": "Vehicle",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "location", "value": {"latitude": 48.8566, "longitude": 2.3522}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_invalid_json_input(self):
        """Test the function's response to invalid JSON input."""
        rdf_jsonld = "This is not a valid JSON"
        with self.assertRaises(json.JSONDecodeError):
            rdf_jsonld_to_ngsild(rdf_jsonld)

    def test_empty_jsonld(self):
        """Test the conversion of an empty JSON-LD document."""
        rdf_jsonld = json.dumps({})
        expected_ngsild = {
            "id": "urn:ngsi-ld:unknown:id",
            "type": "UnknownType",
            "@context": "https://schema.lab.fiware.org/ld/context",
            "attributes": []
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

if __name__ == '__main__':
    unittest.main()