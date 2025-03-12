from typing import Dict
import json
from rdflib import Graph, Literal, RDF, RDFS, URIRef

def rdf_jsonld_to_ngsild(rdf_jsonld: str) -> Dict:
    # Create an RDF Graph from the RDF JSON-LD string
    g = Graph().parse(data=rdf_jsonld, format="json-ld")

    # Initialize an empty NGSI-LD dictionary
    ngsild = {}

    # Iterate through the triples in the RDF Graph
    for s, p, o in g:
        # Check if the triple represents a property of the context
        if p == RDF.type and o == RDFS.Resource:
            # Get the context URI
            context_uri = str(s)

        # Check if the triple represents a property of a thing
        elif p.startswith("http://www.w3.org/ns/"):
            # Get the property name and value
            property_name = str(p)
            property_value = str(o)

            # If the context URI is defined, add the property to the NGSI-LD dictionary
            if context_uri:
                if context_uri not in ngsild:
                    ngsild[context_uri] = {}
                ngsild[context_uri][property_name] = property_value

    # Convert the NGSI-LD dictionary to a JSON string
    return json.dumps(ngsild, indent=4)
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