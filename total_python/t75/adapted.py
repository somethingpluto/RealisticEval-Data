import os
import re


def rename_files(directory):
    # Helper function to extract the base name without trailing digits and optional hyphen
    def get_base_name(filename):
        return re.sub(r'(\d{3})(-\d)?(?=\.png$)', '', filename)

    # Get list of PNG files in the directory, ensuring case insensitivity
    png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

    # Sort files alphabetically by their names for predictable ordering
    png_files.sort()

    # Print the sorted list of files for verification
    print("Sorted files:")
    for file in png_files:
        print(file)

    # Initialize counters and track previous file base name
    prev_base_name = None
    count = 1

    # Renumerate files with updated sequence numbers
    for filename in png_files:
        base_name = get_base_name(filename)

        # Reset counter when base name changes
        if base_name != prev_base_name:
            count = 1

        new_filename = f"{base_name}{count:03d}.png"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renaming {filename} to {new_filename}")

        # Update trackers
        prev_base_name = base_name
        count += 1
