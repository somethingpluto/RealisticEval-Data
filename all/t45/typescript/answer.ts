interface DateInfo {
    year: number;
    month: string;
    weekOfTheMonth: number;
    dayOfTheWeek: string;
}

function getCurrentDateInfo(testDate?: Date): DateInfo {
    const today = testDate || new Date();

    const year = today.getFullYear();
    const month = today.toLocaleString('default', { month: 'long' });
    const dayOfWeek = today.toLocaleString('default', { weekday: 'long' });

    // Calculate the week of the month
    const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    const firstDayWeekday = firstDayOfMonth.getDay();
    const weekOfMonth = Math.ceil((today.getDate() + firstDayWeekday) / 7);

    return {
        year: year,
        month: month,
        weekOfTheMonth: weekOfMonth,
        dayOfTheWeek: dayOfWeek
    };
}