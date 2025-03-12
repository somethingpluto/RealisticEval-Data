import { toRadians, toDegrees } from './utils';

function calculateBearing(lat1: number, lon1: number, lat2: number, lon2: number): number {
    // Validate input ranges
    if (lat1 < -90 || lat1 > 90 || lat2 < -90 || lat2 > 90 || lon1 < -180 || lon1 > 180 || lon2 < -180 || lon2 > 180) {
        throw new Error('Latitude must be between -90 and 90, and longitude must be between -180 and 180.');
    }

    // Convert latitude and longitude from degrees to radians
    const lat1Rad = toRadians(lat1);
    const lon1Rad = toRadians(lon1);
    const lat2Rad = toRadians(lat2);
    const lon2Rad = toRadians(lon2);

    // Calculate the differences
    const dLon = lon2Rad - lon1Rad;

    // Calculate the bearing
    const y = Math.sin(dLon) * Math.cos(lat2Rad);
    const x = Math.cos(lat1Rad) * Math.sin(lat2Rad) - Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(dLon);
    const bearingRad = Math.atan2(y, x);

    // Convert the bearing from radians to degrees
    const bearingDeg = toDegrees(bearingRad);

    // Normalize the bearing to be within 0 to 360 degrees
    return (bearingDeg + 360) % 360;
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
