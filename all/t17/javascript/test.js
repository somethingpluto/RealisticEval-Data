describe('Haversine Distance', () => {
    it('should return a distance of 0 for the same point', () => {
        const lat = 52.2296756;
        const lon = 21.0122287;
        const result = haversineDistance(lat, lon, lat, lon);
        expect(result).toBeCloseTo(0.0, 6);
    });

    it('should calculate small distance for points very close together', () => {
        const lat1 = 52.2296756;
        const lon1 = 21.0122287; // Warsaw, Poland
        const lat2 = 52.2296756;
        const lon2 = 21.0122297; // Very close to the previous point
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(0.0001, 4); // Expected small distance
    });

    it('should calculate large distance for far apart points', () => {
        const lat1 = 52.2296756;
        const lon1 = 21.0122287; // Warsaw, Poland
        const lat2 = 41.8919300;
        const lon2 = 12.5113300; // Rome, Italy
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(1315.514, 2); // Approx distance in km
    });

    it('should calculate distance on the equator', () => {
        const lat1 = 0.0;
        const lon1 = 0.0; // Gulf of Guinea (Equator and Prime Meridian intersection)
        const lat2 = 0.0;
        const lon2 = 90.0; // On the Equator, 90 degrees east
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(10007.54, 2); // Approx quarter of Earth's circumference
    });

    it('should calculate distance from North Pole to South Pole', () => {
        const lat1 = 90.0;
        const lon1 = 0.0; // North Pole
        const lat2 = -90.0;
        const lon2 = 0.0; // South Pole
        const result = haversineDistance(lat1, lon1, lat2, lon2);
        expect(result).toBeCloseTo(20015.09, 2); // Approx half of Earth's circumference
    });
});