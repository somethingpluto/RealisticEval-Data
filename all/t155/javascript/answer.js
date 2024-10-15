export const getTimestamp = (createdAt) => {
    const now = new Date();
    const diffInSeconds = Math.floor((now.getTime() - createdAt.getTime()) / 1000);

    // Define time intervals in seconds
    const intervals = {
        year: 31536000,
        month: 2592000,
        week: 604800,
        day: 86400,
        hour: 3600,
        minute: 60,
    };

    // Determine the most appropriate time interval and its unit
    let intervalCount;
    let intervalUnit;

    if (diffInSeconds >= intervals.year) {
        intervalCount = Math.floor(diffInSeconds / intervals.year);
        intervalUnit = intervalCount === 1 ? 'year' : 'years';
    } else if (diffInSeconds >= intervals.month) {
        intervalCount = Math.floor(diffInSeconds / intervals.month);
        intervalUnit = intervalCount === 1 ? 'month' : 'months';
    } else if (diffInSeconds >= intervals.week) {
        intervalCount = Math.floor(diffInSeconds / intervals.week);
        intervalUnit = intervalCount === 1 ? 'week' : 'weeks';
    } else if (diffInSeconds >= intervals.day) {
        intervalCount = Math.floor(diffInSeconds / intervals.day);
        intervalUnit = intervalCount === 1 ? 'day' : 'days';
    } else if (diffInSeconds >= intervals.hour) {
        intervalCount = Math.floor(diffInSeconds / intervals.hour);
        intervalUnit = intervalCount === 1 ? 'hour' : 'hours';
    } else if (diffInSeconds >= intervals.minute) {
        intervalCount = Math.floor(diffInSeconds / intervals.minute);
        intervalUnit = intervalCount === 1 ? 'minute' : 'minutes';
    } else {
        intervalCount = diffInSeconds;
        intervalUnit = intervalCount === 1 ? 'second' : 'seconds';
    }

    return `${intervalCount} ${intervalUnit} ago`;
};