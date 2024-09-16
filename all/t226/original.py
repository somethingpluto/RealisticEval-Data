# Created using ChatGPT

import json

# Open the TSV file for reading and the JSONL file for writing
with open('sashank.tsv', 'r') as tsvfile, open('sashank.jsonl', 'w') as jsonlfile:
    # Read the header line from the TSV file and split it into column names
    header = tsvfile.readline().strip().split('\t')
    # Find the indexes of the columns we need
    # basis_idx = header.index('Basis')
    premise_idx = header.index('premise')
    hypothesis_idx = header.index('hypothesis')
    true_label_idx = header.index('label')
    # new_premises_idx = header.index('New Premise')
    # new_label_idx = header.index('New Label')
    # Loop over the remaining lines in the TSV file
    for line in tsvfile:
        # Split the line into fields
        fields = line.strip().split('\t')
        # Extract the fields we need
        new_premise = fields[premise_idx]
        hypothesis = fields[hypothesis_idx]
        new_label = fields[true_label_idx]
        # Create a dictionary with the desired attributes
        instance = {'premise': new_premise,
                    'hypothesis': hypothesis,
                    'label': new_label}
        # Write the instance as a JSON string to the JSONL file
        jsonlfile.write(json.dumps(instance) + '\n')