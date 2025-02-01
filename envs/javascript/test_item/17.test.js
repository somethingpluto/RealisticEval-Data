/**
 * Calculate the distance between two points on the Earth based on their latitude and longitude.
 * 
 * @param {number} lat1 - Latitude of the first point in degrees.
 * @param {number} lon1 - Longitude of the first point in degrees.
 * @param {number} lat2 - Latitude of the second point in degrees.
 * @param {number} lon2 - Longitude of the second point in degrees.
 * @returns {number} Distance between the two points in kilometers.
 */
function haversineDistance(lat1, lon1, lat2, lon2) {
    const toRadians = (degrees) => degrees * (Math.PI / 180);

    const R = 6371; // Radius of the Earth in kilometers

    const dLat = toRadians(lat2 - lat1);
    const dLon = toRadians(lon2 - lon1);

    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return R * c;
}
describe('TestHaversineDistance', () => {
    it('should return a distance of 0 for the same point', () => {
        const lat = 52.2296756;
        const lon = 21.0122287;
        const result = haversineDistance(lat, lon, lat, lon);
        expect(result).toBeCloseTo(0.0, 6);
    });

    it('should return a small distance for points very close together', () => {
        const lat1 = 52.2296756;
        const lon1 = 21.0122287;  // Warsaw, Poland
        const lat2 = 52.2296756;
        const lon2 = 21.0122297;  // Very close to the previous point
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(0.0001, 4);
    });

    it('should return a large distance for points far apart', () => {
        const lat1 = 52.2296756;
        const lon1 = 21.0122287;  // Warsaw, Poland
        const lat2 = 41.8919300;
        const lon2 = 12.5113300;  // Rome, Italy
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(1315.514, 2);
    });

    it('should return the correct distance for points on the equator', () => {
        const lat1 = 0.0;
        const lon1 = 0.0;  // Gulf of Guinea (Equator and Prime Meridian intersection)
        const lat2 = 0.0;
        const lon2 = 90.0;  // On the Equator, 90 degrees east
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(10007.54, 2);
    });

    it('should return the correct distance from North Pole to South Pole', () => {
        const lat1 = 90.0;
        const lon1 = 0.0;  // North Pole
        const lat2 = -90.0;
        const lon2 = 0.0;  // South Pole
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(20015.09, 2);
    });
});
