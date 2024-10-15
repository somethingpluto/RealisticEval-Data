/**
 * Convert an RGB color object to a HEX color string.
 * @param rgb - A struct containing the red, green, and blue components of the color.
 * @returns A string representing the HEX color code.
 */
std::string rgbToHex(const RGB& rgb);

/**
 * Convert a HEX color string to an RGB color object.
 * @param hex - A string representing the HEX color code.
 * @returns An optional struct containing the red, green, and blue components of the color, or nullopt if the HEX code is invalid.
 */
std::optional<RGB> hexToRgb(const std::string& hex);