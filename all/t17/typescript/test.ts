import { haversineDistance } from './haversineDistance';  // Assuming your distance function is in haversineDistance.ts

describe('haversineDistance', () => {

    it('should return 0 for the same point', () => {
        // Same point should return a distance of 0
        const lat = 52.2296756, lon = 21.0122287;
        const result = haversineDistance(lat, lon, lat, lon);
        expect(result).toBeCloseTo(0.0, 6);
    });

    it('should return a small distance for points that are very close together', () => {
        // Points that are very close together (few meters apart)
        const lat1 = 52.2296756, lon1 = 21.0122287;  // Warsaw, Poland
        const lat2 = 52.2296756, lon2 = 21.0122297;  // Very close to the previous point
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(0.0001, 4);  // Expected small distance
    });

    it('should return a large distance for far apart points', () => {
        // Points that are far apart
        const lat1 = 52.2296756, lon1 = 21.0122287;  // Warsaw, Poland
        const lat2 = 41.8919300, lon2 = 12.5113300;  // Rome, Italy
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(1315.514, 2);  // Approx distance in km
    });

    it('should return distance for points on the equator', () => {
        // Points on the equator
        const lat1 = 0.0, lon1 = 0.0;  // Gulf of Guinea (Equator and Prime Meridian intersection)
        const lat2 = 0.0, lon2 = 90.0;  // On the Equator, 90 degrees east
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(10007.54, 2);  // Approx quarter of Earth's circumference
    });

    it('should return distance from North Pole to South Pole', () => {
        // Distance from North Pole to South Pole
        const lat1 = 90.0, lon1 = 0.0;  // North Pole
        const lat2 = -90.0, lon2 = 0.0;  // South Pole
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(20015.09, 2);  // Approx half of Earth's circumference
    });

});