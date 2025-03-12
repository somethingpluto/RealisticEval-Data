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
    const currentDate = new Date();
    const messageTime = messageDate.getTime();
    const currentTime = currentDate.getTime();

    const oneDay = 24 * 60 * 60 * 1000;
    const oneWeek = 7 * oneDay;

    const timeDifference = currentTime - messageTime;

    if (timeDifference < oneDay && messageDate.getDate() === currentDate.getDate()) {
        return "Today";
    } else if (timeDifference < 2 * oneDay && messageDate.getDate() === currentDate.getDate() - 1) {
        return "Yesterday";
    } else if (timeDifference < oneWeek) {
        const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        return daysOfWeek[messageDate.getDay()];
    } else {
        const year = messageDate.getFullYear();
        const month = String(messageDate.getMonth() + 1).padStart(2, '0');
        const day = String(messageDate.getDate()).padStart(2, '0');
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
