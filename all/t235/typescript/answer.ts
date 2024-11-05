import { radians, sin, cos, atan2, degrees } from 'mathjs';

/**
 * Calculate the bearing from one latitude and longitude to another.
 *
 * @param lat1 - Latitude of the starting point in decimal degrees.
 * @param lon1 - Longitude of the starting point in decimal degrees.
 * @param lat2 - Latitude of the ending point in decimal degrees.
 * @param lon2 - Longitude of the ending point in decimal degrees.
 * @returns The bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
 */
function calculateBearing(lat1: number, lon1: number, lat2: number, lon2: number): number {
    // Convert latitude and longitude from degrees to radians
    const lat1Rad = radians(lat1);
    const lon1Rad = radians(lon1);
    const lat2Rad = radians(lat2);
    const lon2Rad = radians(lon2);

    // Difference in longitude
    const deltaLonRad = lon2Rad - lon1Rad;

    // Calculate the bearing components
    const x = sin(deltaLonRad) * cos(lat2Rad);
    const y = cos(lat1Rad) * sin(lat2Rad) - (sin(lat1Rad) * cos(lat2Rad) * cos(deltaLonRad));

    // Calculate the initial bearing in radians
    const initialBearingRad = atan2(x, y);

    // Convert the initial bearing from radians to degrees
    const initialBearingDeg = degrees(initialBearingRad);

    // Normalize the bearing to 0-360 degrees
    const compassBearing = (initialBearingDeg + 360) % 360;

    return compassBearing;
}