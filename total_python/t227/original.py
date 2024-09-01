from PIL.Image import Image


def count_colors(image_paths):
    color_counter = Counter()

    for path in tqdm(image_paths, desc="Processing images"):
        image = Image.open(path)
        # Convert the image to RGB if it's not
        image = image.convert('RGB')
        colors = image.getdata()
        color_counter.update(colors)

    return color_counter