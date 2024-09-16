# GENERATED WITH CHATGPT WITH THE FOLLOWING PROMPT

###i have this csv with question in it, but i left some empty rows that i want to remove. I think effectively i want to delete lines that end in ",,". can you give me a code, script, or other method to do this? the question look like this: (data_pure.csv)

import csv

# Open the CSV file for reading
with open('./data_pure.csv', 'r') as csvfile:
    # Create a csv reader object
    reader = csv.reader(csvfile)
    
    # Open a new file to write the filtered question
    with open('filtered_data.csv', 'w', newline='') as outfile:
        # Create a csv writer object
        writer = csv.writer(outfile)
        
        # Iterate through each row in the CSV file
        for row in reader:
            # Check if the last two elements of the row are empty
            if row[-2:] == ["", ""]:
                # Skip this row
                continue
            
            # Write the row to the output file
            writer.writerow(row)