import json


def rdf_jsonld_to_ngsild(rdf_jsonld):
    """
    Convert RDF JSON-LD data to NGSI-LD format.

    Args:
    rdf_jsonld (str or dict): RDF JSON-LD formatted data as a string or dict.

    Returns:
    dict: Data formatted according to NGSI-LD specifications.
    """
    if isinstance(rdf_jsonld, str):
        rdf_jsonld = json.loads(rdf_jsonld)

    ngsi_ld = {
        "id": rdf_jsonld.get("@id", "urn:ngsi-ld:unknown:id"),
        "type": rdf_jsonld.get("@type", "UnknownType"),
        "@context": rdf_jsonld.get("@context", "https://schema.lab.fiware.org/ld/context"),
        "attributes": []
    }

    # Assuming simple attribute structure conversion
    for key, value in rdf_jsonld.items():
        if key not in ["@context", "@id", "@type"]:
            ngsi_ld["attributes"].append({
                "type": "Property",
                "name": key,
                "value": value
            })

    return ngsi_ld
