import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private BloomFilter bloomFilter;

    @BeforeEach
    public void setUp() {
        bloomFilter = new BloomFilter(100, 3); // Adjust size and hash count as needed
    }

    @Test
    public void testAddAndContains() {
        String item = "testItem";
        bloomFilter.add(item);

        assertTrue(bloomFilter.contains(item));
    }

    @Test
    public void testFalsePositive() {
        String item1 = "item1";
        String item2 = "item2";

        bloomFilter.add(item1);

        assertFalse(bloomFilter.contains(item2));
    }

    @Test
    public void testMultipleAdds() {
        String item1 = "item1";
        String item2 = "item2";

        bloomFilter.add(item1);
        bloomFilter.add(item2);

        assertTrue(bloomFilter.contains(item1));
        assertTrue(bloomFilter.contains(item2));
    }
}