// Start of the code context
import { Point } from './Point';

/**
 * Calculates the distance between two points on the Earth's surface using the Haversine formula.
 * 
 * @param point1 - The first point with latitude and longitude.
 * @param point2 - The second point with latitude and longitude.
 * @returns The distance between the two points in kilometers.
 */
function haversineDistance(point1: Point, point2: Point): number {
    // ... (rest of the function remains unchanged)
}

// End of the code context
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
