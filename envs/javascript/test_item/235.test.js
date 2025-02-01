/**
 * Calculates the azimuth between two points on the Earth.
 * This function accepts the latitude and longitude of the two points as parameters and returns the azimuth from the first point to the second point in degrees.
 * 
 * @param {number} lat1 - Latitude of the starting point in decimal degrees.
 * @param {number} lon1 - Longitude of the starting point in decimal degrees.
 * @param {number} lat2 - Latitude of the ending point in decimal degrees.
 * @param {number} lon2 - Longitude of the ending point in decimal degrees.
 * @returns {number} Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
 */
function calculateBearing(lat1, lon1, lat2, lon2) {
    // Convert the latitudes and longitudes from degrees to radians
    const toRadians = (degrees) => degrees * (Math.PI / 180);
    const lat1Rad = toRadians(lat1);
    const lon1Rad = toRadians(lon1);
    const lat2Rad = toRadians(lat2);
    const lon2Rad = toRadians(lon2);

    // Calculate the differences in the latitudes and longitudes
    const deltaLat = lat2Rad - lat1Rad;
    const deltaLon = lon2Rad - lon1Rad;

    // Calculate the azimuth using the haversine formula
    let y = Math.sin(deltaLon) * Math.cos(lat2Rad);
    let x = Math.cos(lat1Rad) * Math.sin(lat2Rad) - Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(deltaLon);
    let brng = Math.atan2(y, x);

    // Convert the bearing from radians to degrees
    brng = (brng * 180 / Math.PI + 360) % 360;

    return brng;
}
describe('TestCalculateBearing', () => {
    it('should calculate north bearing correctly', () => {
        // From equator directly north
        expect(calculateBearing(0, 0, 10, 0)).toBeCloseTo(0);
    });

    it('should calculate east bearing correctly', () => {
        // From prime meridian directly east
        expect(calculateBearing(0, 0, 0, 10)).toBeCloseTo(90);
    });

    it('should calculate south bearing correctly', () => {
        // From a point directly south
        expect(calculateBearing(10, 0, 0, 0)).toBeCloseTo(180);
    });

    it('should calculate west bearing correctly', () => {
        // From a point directly west
        expect(calculateBearing(0, 10, 0, 0)).toBeCloseTo(270);
    });

    it('should calculate bearing across prime meridian correctly', () => {
        // From a point west of the prime meridian to a point east
        expect(calculateBearing(0, -1, 0, 1)).toBeCloseTo(90);
    });
});
