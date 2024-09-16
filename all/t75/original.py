import os
import re


def rename_files(directory):
    # Get list of PNG files in the directory
    png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

    # Sort files alphabetically by their names
    png_files.sort()

    # Print the sorted list of files
    print("Sorted files:")
    for file in png_files:
        print(file)

    # Renumerate files
    prev_base_name = None
    count = 1
    for filename in png_files:
        # Extract base name without postfix and number
        base_name = re.sub(r'(\d{3})(-\d)?(?=\.png$)', '', filename)

        if base_name != prev_base_name:
            count = 1

        new_filename = f"{base_name}{count:03d}.png"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renaming {filename} to {new_filename}")

        prev_base_name = base_name
        count += 1
