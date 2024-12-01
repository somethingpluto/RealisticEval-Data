package org.real.temp;

public class Answer {

    /**
     * Calculate the bearing from one latitude and longitude to another.
     *
     * @param lat1 Latitude of the starting point in decimal degrees.
     * @param lon1 Longitude of the starting point in decimal degrees.
     * @param lat2 Latitude of the ending point in decimal degrees.
     * @param lon2 Longitude of the ending point in decimal degrees.
     * @return Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
     */
    public static double calculateBearing(double lat1, double lon1, double lat2, double lon2) {
        // Convert latitude and longitude from degrees to radians
        double lat1Rad = Math.toRadians(lat1);
        double lon1Rad = Math.toRadians(lon1);
        double lat2Rad = Math.toRadians(lat2);
        double lon2Rad = Math.toRadians(lon2);

        // Difference in longitude
        double deltaLonRad = lon2Rad - lon1Rad;

        // Calculate the bearing components
        double x = Math.sin(deltaLonRad) * Math.cos(lat2Rad);
        double y = Math.cos(lat1Rad) * Math.sin(lat2Rad) - (Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(deltaLonRad));

        // Calculate the initial bearing in radians
        double initialBearingRad = Math.atan2(x, y);

        // Convert the initial bearing from radians to degrees
        double initialBearingDeg = Math.toDegrees(initialBearingRad);

        // Normalize the bearing to 0-360 degrees
        double compassBearing = (initialBearingDeg + 360) % 360;

        return compassBearing;
    }

    public static void main(String[] args) {
        // Example usage
        double lat1 = 51.5074; // London
        double lon1 = -0.1278;
        double lat2 = 40.7128; // New York
        double lon2 = -74.0060;

        double bearing = calculateBearing(lat1, lon1, lat2, lon2);
        System.out.println("Bearing: " + bearing + " degrees");
    }
}