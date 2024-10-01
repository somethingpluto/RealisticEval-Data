/**
 * Checks if the string conforms to the latitude and longitude identification specification.
 *
 * @param coord - The coordinate string to check (can be latitude or longitude).
 * @returns A boolean indicating whether the coordinate is valid.
 */
const isValidCoordinate = (coord: string): boolean => {
    // Regular expression for latitude and longitude
    const latitudeRegex = /^[-+]?([1-8]?[0-9](\.\d+)?|90(\.0+)?)([NnSs]?)$/; // -90 to 90 degrees
    const longitudeRegex = /^[-+]?((1[0-7][0-9]|[0-9]?[0-9])(\.\d+)?|180(\.0+)?)([EeWw]?)$/; // -180 to 180 degrees

    // Check if the coordinate matches latitude or longitude format
    return latitudeRegex.test(coord) || longitudeRegex.test(coord);
};
