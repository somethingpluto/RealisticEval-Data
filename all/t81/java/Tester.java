public class Tester {

    /**
     * Tests basic functionality of the findClosestElement method.
     */
    @Test
    public void testBasicFunctionality() {
        assertEquals("Should return 3 as it is the first closest element to 5",
                     3, findClosestElement(5, List.of(1, 3, 7, 8, 9)).intValue());
    }

    /**
     * Tests the exact match scenario for the findClosestElement method.
     */
    @Test
    public void testExactMatch() {
        assertEquals("Should return 7 as it exactly matches the target",
                     7, findClosestElement(7, List.of(1, 3, 7, 8, 9)).intValue());
    }

    /**
     * Tests multiple closest values scenario for the findClosestElement method.
     */
    @Test
    public void testMultipleClosestValues() {
        assertEquals("Should return 4 as it is the first closest element to 5",
                     4, findClosestElement(5, List.of(4, 6, 8, 9)).intValue());
    }

    /**
     * Tests float values scenario for the findClosestElement method.
     */
    @Test
    public void testFloatValues() {
        assertEquals("Should return 3.3 as it is the first closest element to 5.5",
                     3.3, findClosestElement(5.5, List.of(1.1, 3.3, 7.7, 8.8)).doubleValue(), 0.001);
    }
}
