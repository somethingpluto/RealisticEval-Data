from typing import Dict


def rdf_jsonld_to_ngsild(rdf_jsonld: str) -> Dict:
    """
    convert the question in RDF JSON-LD format to NGSI-LD format
    Args:
        rdf_jsonld (str): RDF JSON-LD formatted question as a string.

    Returns:
        Data formatted according to NGSI-LD specifications.
    """
