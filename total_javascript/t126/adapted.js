/**
 * Calculates the great-circle distance between two points on the Earth
 * using their latitude and longitude based on the Haversine formula.
 *
 * @param {number} lat1 - Latitude of the first point in degrees.
 * @param {number} lon1 - Longitude of the first point in degrees.
 * @param {number} lat2 - Latitude of the second point in degrees.
 * @param {number} lon2 - Longitude of the second point in degrees.
 * @returns {number} The distance between the two points in kilometers.
 */
function calculateDistance(lat1, lon1, lat2, lon2) {
    const earthRadiusKm = 6371; // Radius of the Earth in kilometers

    // Helper function to convert degrees to radians
    const toRadians = (degrees) => (Math.PI * degrees) / 180;

    // Convert all degrees to radians
    const lat1Rad = toRadians(lat1);
    const lon1Rad = toRadians(lon1);
    const lat2Rad = toRadians(lat2);
    const lon2Rad = toRadians(lon2);

    // Differences in coordinates
    const deltaLat = lat2Rad - lat1Rad;
    const deltaLon = lon2Rad - lon1Rad;

    // Haversine formula
    const a = Math.sin(deltaLat / 2) ** 2 +
              Math.cos(lat1Rad) * Math.cos(lat2Rad) *
              Math.sin(deltaLon / 2) ** 2;

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    // Distance in kilometers
    return earthRadiusKm * c;
}