// spatialWeight.ts
export function spatialWeight(spatial_diff: number, sigma_space: number): number {
  if (sigma_space === 0) {
    throw new Error('sigma_space cannot be zero.');
  }
  return Math.exp(- (spatial_diff ** 2) / (2 * sigma_space ** 2));
}

// spatialWeight.test.ts
import { spatialWeight } from './spatialWeight';

describe('spatialWeight', () => {
  it('calculates the correct weight for given spatial_diff and sigma_space', () => {
    expect(spatialWeight(1, 1)).toBeCloseTo(Math.exp(-0.5));
  });

  it('throws an error when sigma_space is zero', () => {
    expect(() => spatialWeight(1, 0)).toThrow('sigma_space cannot be zero.');
  });
});
describe("Spatial Weight Calculation Tests", () => {
    
    test("Zero Spatial Difference", () => {
        // When spatial difference is zero, weight should be 1
        const spatial_diff = 0.0;
        const sigma_space = 1.0; // arbitrary sigma value
        expect(spatialWeight(spatial_diff, sigma_space)).toBeCloseTo(1.0, 3); // Using 3 decimal places
    });

    test("Positive Spatial Difference", () => {
        // A positive spatial difference with a reasonable sigma
        const spatial_diff = 2.0;
        const sigma_space = 2.0;
        const expected_weight = Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        expect(spatialWeight(spatial_diff, sigma_space)).toBeCloseTo(expected_weight, 3);
    });

    test("Negative Spatial Difference", () => {
        // A negative spatial difference should yield the same weight as positive
        const spatial_diff = -2.0;
        const sigma_space = 2.0;
        const expected_weight = Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        expect(spatialWeight(spatial_diff, sigma_space)).toBeCloseTo(expected_weight, 3);
    });

    test("Small Sigma Space", () => {
        // Test with a small sigma value
        const spatial_diff = 1.0;
        const sigma_space = 0.1;
        const expected_weight = Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        expect(spatialWeight(spatial_diff, sigma_space)).toBeCloseTo(expected_weight, 3);
    });

    test("Large Sigma Space", () => {
        // Test with a large sigma value
        const spatial_diff = 1.0;
        const sigma_space = 100.0;
        const expected_weight = Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        expect(spatialWeight(spatial_diff, sigma_space)).toBeCloseTo(expected_weight, 3);
    });

});
