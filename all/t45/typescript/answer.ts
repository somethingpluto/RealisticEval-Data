import { DateTime } from 'luxon';

function get Current_Date_Info(testDate?: DateTime): { year: number; month: string; week_of_the_month: number; day_of_the_week: string } {
    const today = testDate ? testDate.toJSDate() : DateTime.local().toJSDate();

    const year = today.getFullYear();
    const month = DateTime.local(today.getFullYear(), today.getMonth() + 1).toFormat('MMMM');
    const dayOfWeek = DateTime.local(today.getFullYear(), today.getMonth() + 1, today.getDate()).toFormat('cccc');

    // Calculate the week of the month
    const firstDayOfMonth = DateTime.local(today.getFullYear(), today.getMonth() + 1, 1);
    const firstDayWeekday = firstDayOfMonth.weekday;
    const weekOfMonth = Math.ceil((today.getDate() + firstDayWeekday - 1) / 7);

    return {
        year,
        month,
        week_of_the_month: weekOfMonth,
        day_of_the_week: dayOfWeek
    };
}