/**
 * Returns a string representing the relative time since the given message was created.
 *
 * - If the message was created today, it returns "Today".
 * - If the message was created yesterday, it returns "Yesterday".
 * - If the message was created within the past week (but not today or yesterday),
 *   it returns the corresponding day of the week (e.g., "Monday").
 * - If the message was created earlier than one week ago, it returns a formatted date string
 *   (e.g., "YYYY/MM/DD").
 *
 * @param messageDate - The date when the message was created. This should be a valid Date object.
 * @returns A string indicating the relative time from the current date to the message creation date.
 */
function getRelativeTime(messageDate) {
  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  const messageDay = new Date(messageDate.getFullYear(), messageDate.getMonth(), messageDate.getDate());

  if (messageDay.getTime() === today.getTime()) {
    return "Today";
  } else if (messageDay.getTime() === yesterday.getTime()) {
    return "Yesterday";
  } else if (now.getTime() - messageDay.getTime() < 7 * 24 * 60 * 60 * 1000) {
    const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    return daysOfWeek[messageDay.getDay()];
  } else {
    const year = messageDate.getFullYear();
    const month = (messageDate.getMonth() + 1).toString().padStart(2, '0');
    const day = messageDate.getDate().toString().padStart(2, '0');
    return `${year}/${month}/${day}`;
  }
}
describe('getRelativeTime', () => {
    beforeAll(() => {
        // Mock the current date to ensure consistent test results
        jest.useFakeTimers().setSystemTime(new Date('2024-10-01'));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('should return "Today" for a message created today', () => {
        const messageDate = new Date(); // Current date
        expect(getRelativeTime(messageDate)).toBe("Today");
    });

    test('should return "Yesterday" for a message created yesterday', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24); // Yesterday
        expect(getRelativeTime(messageDate)).toBe("Yesterday");
    });

    test('should return formatted date string for a message created 10 days ago', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24 * 10); // 10 days ago
        expect(getRelativeTime(messageDate)).toBe("2024/09/21"); // Adjust based on the mock date
    });

    test('should return formatted date string for a message created 15 days ago', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24 * 15); // 15 days ago
        expect(getRelativeTime(messageDate)).toBe("2024/09/16"); // Adjust based on the mock date
    });
});
