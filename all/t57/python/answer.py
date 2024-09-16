from PIL import Image


def convert_png_to_ico(png_file_path, ico_file_path, icon_sizes=[(32, 32)]):
    """
    Convert a PNG image file to an ICO format file.

    Args:
    png_file_path (str): Path to the source PNG image file.
    ico_file_path (str): Path to save the ICO file.
    icon_sizes (list): List of tuples specifying the sizes to include in the ICO file.
    """
    # Open the image file using Pillow
    with Image.open(png_file_path) as img:
        # Convert the image to ICO and save it
        img.save(ico_file_path, format='ICO', sizes=icon_sizes)