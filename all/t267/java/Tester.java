import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.real.temp.Answer;

public class Tester {

    @Test
    public void testStandardFqdn() {
        // Test a typical FQDN
        SimpleEntry<String, String> result = Answer.extractSldTld("www.example.com");
        assertEquals(new SimpleEntry<>("example", "com"), result);
    }

    @Test
    public void testStandardFqdn2() {
        // Test a typical FQDN
        SimpleEntry<String, String> result = Answer.extractSldTld("www.example.xyz");
        assertEquals(new SimpleEntry<>("example", "xyz"), result);
    }

    @Test
    public void testFqdnWithSubdomains() {
        // Test an FQDN with multiple subdomains
        SimpleEntry<String, String> result = Answer.extractSldTld("blog.subdomain.example.com");
        assertEquals(new SimpleEntry<>("example", "com"), result);
    }

    @Test
    public void testNumericTld() {
        // Test a numeric TLD, which can occur in private networks
        SimpleEntry<String, String> result = Answer.extractSldTld("server.example.123");
        assertEquals(new SimpleEntry<>("example", "123"), result);
    }
}