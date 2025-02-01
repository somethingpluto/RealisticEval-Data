/**
 * Converts a date string from the format 'ddd, dd mmm yyyy HH:MM:ss ZZ (zzz)'
 * to the format 'yyyy-mm-dd_HH:MM:ss'.
 *
 * @param {string} dateStr - The input date string.
 * @returns {string | null} - The formatted date string in the format 'yyyy-mm-dd_HH:MM:SS', or null if the input date string is invalid.
 */
function formatDateString(dateStr) {
    const dateRegex = /^([a-zA-Z]{3}),\s+(\d{2})\s+([a-zA-Z]{3})\s+(\d{4})\s+(\d{2}):(\d{2}):(\d{2})\s+([+\-]\d{4})\s+\((\w+)\)$/;
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    const match = dateStr.match(dateRegex);
    if (!match) {
        return null;
    }

    const day = match[2];
    const month = monthNames.indexOf(match[3]) + 1;
    const year = match[4];
    const hours = match[5];
    const minutes = match[6];
    const seconds = match[7];
    const timezoneOffset = match[8];

    const formattedDate = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}_${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

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
