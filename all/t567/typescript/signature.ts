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
function getRelativeTime(messageDate: Date): string {
}