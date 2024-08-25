from typing import Dict


def rdf_jsonld_to_ngsild(rdf_jsonld: str) -> Dict:
    """
    convert the data in RDF JSON-LD format to NGSI-LD format
    Args:
        rdf_jsonld (str): RDF JSON-LD formatted data as a string.

    Returns:
        Data formatted according to NGSI-LD specifications.
    """
