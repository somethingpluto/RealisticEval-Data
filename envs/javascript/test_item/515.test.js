/**
 * Converts a date string from the format 'ddd, dd mmm yyyy HH:MM:ss ZZ (zzz)'
 * to the format 'yyyy-mm-dd_HH:MM:ss'.
 *
 * @param {string} dateStr - The input date string.
 * @returns {string | null} - The formatted date string in the format 'yyyy-mm-dd_HH:MM:SS', or null if the input date string is invalid.
 */
function formatDateString(dateStr) {
    // Define the regex pattern to match the input date format
    const pattern = /^(\w{3}), (\d{2}) (\w{3}) (\d{4}) (\d{2}):(\d{2}):(\d{2}) ([+-]\d{4}) \((\w{3})\)$/;
    
    // Match the input string against the pattern
    const match = dateStr.match(pattern);
    
    // If the input string does not match the pattern, return null
    if (!match) {
        return null;
    }
    
    // Extract the components of the date string
    const [_, dayOfWeek, day, month, year, hours, minutes, seconds, timezone, timezoneAbbr] = match;
    
    // Create a new Date object using the extracted components
    const date = new Date(`${month} ${day}, ${year} ${hours}:${minutes}:${seconds} ${timezone}`);
    
    // Check if the date is valid
    if (isNaN(date.getTime())) {
        return null;
    }
    
    // Format the date to the desired output format
    const formattedDate = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}_${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}:${String(date.getSeconds()).padStart(2, '0')}`;
    
    return formattedDate;
}
describe('TestFormatDateString', () => {
    it('test_valid_date_conversion', () => {
        // Test case for a valid date string.
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)";
        const expectedDate = "2023-09-28_14:45:00";
        expect(formatDateString(dateStr)).toEqual(expectedDate);
    });

    it('test_invalid_date_format', () => {
        // Test case for an invalid date string format.
        const dateStr = "Invalid date format";
        expect(formatDateString(dateStr)).toBeNull();
    });

    it('test_missing_components', () => {
        // Test case for a date string missing components.
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000";
        expect(formatDateString(dateStr)).toBeNull();
    });

    it('test_edge_case_date', () => {
        // Test case for an edge case date string (e.g., leap year).
        const dateStr = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        const expectedDate = "2024-02-29_14:45:00";
        expect(formatDateString(dateStr)).toEqual(expectedDate);
    });
});
