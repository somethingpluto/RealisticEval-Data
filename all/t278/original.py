def split_image(image, tile_size):
    width, height = image.size
    tiles = []
    
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            box = (x, y, x + tile_size, y + tile_size)
            tile = image.crop(box)
            tiles.append(tile)
    
    return tiles