/**
 * Calculates the time difference between a given date and the current date.
 *
 * @param {Date | string} givenDate - The date to compare against the current date.
 * @returns {Object} - An object containing days, hours, and minutes elapsed.
 * {
 *         days: days,
 *         hours: remainingHours,
 *         minutes: remainingMinutes,
 * }
 */
function calculateTimeDifference(givenDate) {
    // Convert givenDate to a Date object if it's a string
    const dateToCompare = new Date(givenDate);
    const currentDate = new Date();

    // Calculate the difference in milliseconds
    const differenceInMilliseconds = currentDate - dateToCompare;

    // If the given date is in the future
    if (differenceInMilliseconds < 0) {
        return { days: 0, hours: 0, minutes: 0 };
    }

    // Calculate days, hours, and minutes
    const minutes = Math.floor((differenceInMilliseconds / 1000) / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    // Calculate remaining hours and minutes
    const remainingHours = hours % 24;
    const remainingMinutes = minutes % 60;

    return {
        days: days,
        hours: remainingHours,
        minutes: remainingMinutes,
    };
}