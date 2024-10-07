/**
 * Checks if two timestamps correspond to the same day.
 *
 * @param timestamp1 - The first timestamp to compare.
 * @param timestamp2 - The second timestamp to compare.
 * @returns True if both timestamps are on the same day, false otherwise.
 */
function isSameDay(timestamp1: number, timestamp2: number): boolean {
    // Convert timestamps to Date objects
    const date1 = new Date(timestamp1);
    const date2 = new Date(timestamp2);

    // Compare the year, month, and date of both Date objects
    return (
        date1.getFullYear() === date2.getFullYear() &&
        date1.getMonth() === date2.getMonth() &&
        date1.getDate() === date2.getDate()
    );
};