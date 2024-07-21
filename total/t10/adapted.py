from PIL import Image, ImageChops
import numpy as np
import os
from scipy.ndimage import convolve

def generate_difference_visualization(base_image_path, comparison_image_path, output_directory, visibility_threshold=10, contrast_factor=1):
    # Load images and convert to grayscale
    base_image = Image.open(base_image_path).convert('L')
    comparison_image = Image.open(comparison_image_path).convert('L')

    # Compute difference between images
    difference = ImageChops.difference(base_image, comparison_image)

    # Convert difference image to numpy array for processing
    difference_array = np.array(difference)

    # Apply threshold to create a binary difference mask
    difference_array[difference_array <= visibility_threshold] = 0
    difference_array[difference_array > visibility_threshold] = 1

    # Define a 3x3 convolution kernel
    kernel = np.ones((3, 3), dtype=np.float32)

    # Enhance differences by convolving with the kernel
    convolved_differences = convolve(difference_array, kernel, mode='constant', cval=0.0)

    # Scale and apply intensity factor
    convolved_differences = (convolved_differences / convolved_differences.max()) * 255 * contrast_factor
    convolved_differences = np.clip(convolved_differences, 0, 255)

    # Convert back to an image
    final_image = Image.fromarray(convolved_differences.astype('uint8'))

    # Ensure unique filename in the output directory
    unique_counter = 1
    while True:
        output_path = os.path.join(output_directory, f'difference-{unique_counter:04d}.jpg')
        if not os.path.exists(output_path):
            break
        unique_counter += 1

    # Save the resulting image
    final_image.save(output_path)

# Example usage
base_path = "path_to_base_image.jpg"
comparison_path = "path_to_comparison_image.jpg"
output_path = "path_to_output_directory"

generate_difference_visualization(base_path, comparison_path, output_path)
