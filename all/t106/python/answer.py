import re

def is_base64_image(image_data):
    # Check if the input is a non-empty string
    if not isinstance(image_data, str) or image_data.strip() == '':
        return False

    # Regular expression to validate a Base64 image string
    base64_image_pattern = r'^data:image/(jpeg|png|gif|bmp|webp);base64,[A-Za-z0-9+/]+={0,2}$'

    # Test the image data against the pattern
    return re.match(base64_image_pattern, image_data) is not None