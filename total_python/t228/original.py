# Created using ChatGPT

import json
import random

# Set the number of lines to sample
num_lines_to_sample = 25

# Open the JSONL file for reading
with open("./eval_output/long_incorrect.jsonl", "r") as f:
    # Read the lines into a list
    lines = f.readlines()

    # Shuffle the list to randomize the order
    random.shuffle(lines)

    # Sample the first n lines
    sampled_lines = lines[:num_lines_to_sample]

    # Create a new JSONL file for writing
    with open("./eval_output/sample_long_incorrect.jsonl", "w") as output_file:
        # Parse the JSON strings and write the results to the new file
        for line in sampled_lines:
            try:
                # Parse the JSON string
                data = json.loads(line)

                # Write the required attributes to the new file
                output_file.write(json.dumps({"premise": data['premise'], "hypothesis": data['hypothesis'], "label": data['label']}) + "\n")
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing line: {line.strip()}. Skipping to the next line.")

print(f"Randomly sampled {num_lines_to_sample} lines written to './eval_output/sample_long_incorrect.jsonl'.")