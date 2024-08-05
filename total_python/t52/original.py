import os
import sys

def rename_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            old_name = os.path.join(root, file)
            new_name = os.path.join(root, file.replace(':', '-'))
            if old_name != new_name:
                os.rename(old_name, new_name)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python rename_files.py <directory_path>')
        sys.exit(1)

    path = sys.argv[1]
    rename_files(path)