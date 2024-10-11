import os


def simplify_windows_path(path):
    # Replace the drive letter and colon, e.g., 'D:' with 'D_'
    drive, path_without_drive = os.path.splitdrive(path)
    simplified_drive = drive.rstrip(':') + '_'

    # Replace backslashes with underscores and strip any trailing backslash
    simplified_path = path_without_drive.replace('\\', '_').strip('_')

    # Concatenate the simplified drive and the remaining path
    final_path = simplified_drive + simplified_path

    return final_path
