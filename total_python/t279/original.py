def merge_tiles(tiles, tile_size):
    tile_count = len(tiles)
    width = tile_count * tile_size
    height = tile_size
    result_image = Image.new("RGBA", (width, height))  # Specify "RGBA" mode
    
    for i, tile in enumerate(tiles):
        result_image.paste(tile, (i * tile_size, 0))
    
    return result_image