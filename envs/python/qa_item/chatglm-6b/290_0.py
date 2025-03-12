
from typing import Dict

def rdf_jsonld_to_ngsild(rdf_jsonld: str) -> Dict:
    # Convert the RDF JSON-LD string to a dictionary
    rdf_dict = dict(RDF.parse_qdf(rdf_jsonld))

    # Convert the dictionary to a string in NGSI-LD format
    ngsild_string = f"{rdf_dict['subject']}:{rdf_dict['object']} {rdf_dict['property']} {rdf_dict['value']}"

    # Return the string in NGSI-LD format
    return ngsild_string

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