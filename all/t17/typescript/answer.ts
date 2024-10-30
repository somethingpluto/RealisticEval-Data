/**
 * Calculate the distance between two points on the Earth using the Haversine formula.
 *
 * @param lat1 - Latitude of the first point in degrees.
 * @param lon1 - Longitude of the first point in degrees.
 * @param lat2 - Latitude of the second point in degrees.
 * @param lon2 - Longitude of the second point in degrees.
 * @returns Distance between the two points in kilometers.
 */
function haversineDistance(lat1: number, lon1: number, lat2: number, lon2: number): number {
    const R = 6371.0;
    const lat1Rad = degreesToRadians(lat1);
    const lon1Rad = degreesToRadians(lon1);
    const lat2Rad = degreesToRadians(lat2);
    const lon2Rad = degreesToRadians(lon2);
    const dlat = lat2Rad - lat1Rad;
    const dlon = lon2Rad - lon1Rad;
    const a = Math.sin(dlat / 2) ** 2 + Math.cos(lat1Rad) * Math.cos(lat2Rad) * Math.sin(dlon / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c;
    return distance;
}

function degreesToRadians(degrees: number): number {
    return degrees * (Math.PI / 180);
}