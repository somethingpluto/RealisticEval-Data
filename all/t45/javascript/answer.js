const moment = require('moment'); // You need to install moment.js using npm or include it in your HTML file
/**
 * Returns the current time information including year, month, week of the month, and day of the week.
 * Optionally takes a date object for testing purposes.
 *
 * @param {Date} test_date - The date to compute information for, defaults to today's date if not provided.
 *
 * @returns {Object} An object containing the year, month, week of the month, and day of the week.
 */
function get_current_date_info(test_date = null) {

    let today = test_date ? test_date : new Date();

    const year = today.getFullYear();
    const month = moment(today).format('MMMM');
    const day_of_week = moment(today).format('dddd');

    // Calculate the week of the month
    const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    const firstDayWeekday = firstDayOfMonth.getDay();
    const week_of_month = Math.ceil((today.getDate() + firstDayWeekday) / 7);

    return {
        'year': year,
        'month': month,
        'week_of_the_month': week_of_month,
        'day_of_the_week': day_of_week
    };
}