import json

# Written using GPT-4 conversation
# OWL to NGSI-LD Conversion


def rdf_jsonld_to_ngsi_ld(input_file, output_file):
    with open(input_file, 'r') as f:
        rdf_data = json.load(f)

    ngsi_ld_data = []

    for item in rdf_data['@graph']:
        entity = {}
        entity['id'] = item['@id']
        entity['type'] = item['@type'][0]

        for key, value in item.items():
            if key not in ['@id', '@type']:
                if '@value' in value:
                    entity[key] = {
                        'type': 'Property',
                        'value': value['@value']
                    }
                elif '@id' in value:
                    entity[key] = {
                        'type': 'Relationship',
                        'object': value['@id']
                    }
                else:
                    entity[key] = {
                        'type': 'Property',
                        'value': value
                    }

        ngsi_ld_data.append(entity)

    with open(output_file, 'w') as f:
        json.dump(ngsi_ld_data, f, indent=2)