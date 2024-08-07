from PIL import Image, ImageChops
import numpy as np
'''
Generated by GPT-4
'''

import os
from scipy.ndimage import convolve

def compare_images(source_path, compare_path, output_dir, threshold=10, intensity=1):
    # Load the images
    source_image = Image.open(source_path).convert('L')  # convert to grayscale
    compare_image = Image.open(compare_path).convert('L')  # convert to grayscale

    # Find differences
    diff_image = ImageChops.difference(source_image, compare_image)

    # Convert differences to numpy array
    diff_image_np = np.array(diff_image)

    # If pixel is above threshold, set to 1, else set to 0
    diff_image_np[diff_image_np <= threshold] = 0
    diff_image_np[diff_image_np > threshold] = 1

    # Define the 3x3 kernel
    kernel = np.ones((3, 3))

    # Convolve the differences with the kernel
    diff_image_np = convolve(diff_image_np, kernel, mode='constant', cval=0.0)

    # Scale the differences to be between 0 and 255
    diff_image_np = (diff_image_np / diff_image_np.max()) * 255 * intensity

    # Ensure values stay within 0-255 after scaling
    diff_image_np = np.clip(diff_image_np, 0, 255)

    # Convert numpy array to image
    diff_image = Image.fromarray(diff_image_np.astype('uint8'))

    # Generate output path
    counter = 1
    while True:
        output_path = os.path.join(output_dir, f'compare-{counter:04d}.jpg')
        if not os.path.exists(output_path):
            break
        counter += 1

    # Save the image
    diff_image.save(output_path)


# set your params here
base_image = "first-jpg-image.jpg"
comp_image = "image-to-compare-to.jpg"
out_dir = "./outdir"

threshold = 10
intensity = 1

x = compare_images(base_image, comp_image , out_dir, threshold, intensity)