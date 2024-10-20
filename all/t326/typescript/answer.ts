/**
 * Calculates the time difference between a given date and the current date.
 *
 * @param {Date | string} givenDate - The date to compare against the current date.
 * @returns {Object} - An object containing days, hours, and minutes elapsed.
 * {
 *         days: number,
 *         hours: number,
 *         minutes: number,
 * }
 */
function calculateTimeDifference(givenDate: Date | string): { days: number; hours: number; minutes: number } {
    const dateToCompare = new Date(givenDate);
    const currentDate = new Date();

    const differenceInMilliseconds = currentDate.getTime() - dateToCompare.getTime();

    if (differenceInMilliseconds < 0) {
        return { days: 0, hours: 0, minutes: 0 };
    }

    const minutes = Math.floor(differenceInMilliseconds / 1000 / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    const remainingHours = hours % 24;
    const remainingMinutes = minutes % 60;

    return {
        days: days,
        hours: remainingHours,
        minutes: remainingMinutes,
    };
}