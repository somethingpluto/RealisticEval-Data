import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class Tester {

    @Mock
    private LocalDate currentDate;

    private Map<String, Object> result;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
        result = new HashMap<>();
    }

    @Test
    public void testGetCurrentDateInfo() {
        // Mocking the current date
        when(currentDate.getYear()).thenReturn(2024);
        when(currentDate.getMonthValue()).thenReturn(2); // February
        when(currentDate.getDayOfWeek().getValue()).thenReturn(4); // Thursday

        // Call the method under test
        Map<String, Object> actualResult = get_current_date_info(currentDate);

        // Verify the results
        assertEquals(2024, actualResult.get("year"));
        assertEquals("February", actualResult.get("month"));
        assertEquals(1, actualResult.get("week_of_the_month")); // Assuming week starts from 1
        assertEquals("Thursday", actualResult.get("day_of_the_week"));
    }

    // Method to be tested
    private Map<String, Object> get_current_date_info(LocalDate testDate) {
        Map<String, Object> result = new HashMap<>();

        int year = testDate.getYear();
        String month = testDate.getMonth().toString();
        int weekOfMonth = testDate.get(java.time.temporal.WeekFields.of(java.util.Locale.US).weekOfMonth());
        String dayOfWeek = testDate.getDayOfWeek().toString();

        result.put("year", year);
        result.put("month", month);
        result.put("week_of_the_month", weekOfMonth);
        result.put("day_of_the_week", dayOfWeek);

        return result;
    }
}