package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testZeroSpatialDifference() {
        // When spatial difference is zero, weight should be 1
        float spatial_diff = 0.0f;
        float sigma_space = 1.0f; // arbitrary sigma value
        assertEquals(1.0f, Answer.spatialWeight(spatial_diff, sigma_space), 0.001);
    }

    @Test
    public void testPositiveSpatialDifference() {
        // A positive spatial difference with a reasonable sigma
        float spatial_diff = 2.0f;
        float sigma_space = 2.0f;
        float expected_weight = (float) Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        assertEquals(expected_weight, Answer.spatialWeight(spatial_diff, sigma_space), 0.001);
    }

    @Test
    public void testNegativeSpatialDifference() {
        // A negative spatial difference should yield the same weight as positive
        float spatial_diff = -2.0f;
        float sigma_space = 2.0f;
        float expected_weight = (float) Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        assertEquals(expected_weight, Answer.spatialWeight(spatial_diff, sigma_space), 0.001);
    }

    @Test
    public void testSmallSigmaSpace() {
        // Test with a small sigma value
        float spatial_diff = 1.0f;
        float sigma_space = 0.1f;
        float expected_weight = (float) Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        assertEquals(expected_weight, Answer.spatialWeight(spatial_diff, sigma_space), 0.001);
    }

    @Test
    public void testLargeSigmaSpace() {
        // Test with a large sigma value
        float spatial_diff = 1.0f;
        float sigma_space = 100.0f;
        float expected_weight = (float) Math.exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        assertEquals(expected_weight, Answer.spatialWeight(spatial_diff, sigma_space), 0.001);
    }
}