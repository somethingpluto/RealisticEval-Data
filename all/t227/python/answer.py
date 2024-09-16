from PIL import Image

def count_unique_colors(image_path: str) -> int:
    """
    Count the number of unique colors in an image.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - int: The number of unique colors in the image.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Convert the image to RGB mode
            img = img.convert('RGB')
            # Get all the pixels from the image
            pixels = list(img.getdata())
            # Use a set to store unique colors
            unique_colors = set(pixels)
            # Return the number of unique colors
            return len(unique_colors)

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0