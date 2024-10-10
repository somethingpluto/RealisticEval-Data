import { format } from 'date-fns';

interface DateInfo {
    year: number;
    month: string;
    weekOfMonth: number;
    dayOfWeek: string;
}

function getCurrentDateInfo(testDate: Date = new Date()): DateInfo {
    const year = testDate.getFullYear();
    const month = format(testDate, 'MMMM');
    const weekOfMonth = Math.ceil(testDate.getDate() / 7);
    const dayOfWeek = format(testDate, 'dddd');

    return {
        year,
        month,
        weekOfMonth,
        dayOfWeek
    };
}