function calculateTotalSeconds(time) {
    /*
    Calculate the total number of seconds given an array of time periods in the order of
    days, hours, minutes, and seconds.

    :param time: array, where
        time[0] - number of days (optional)
        time[1] - number of hours (optional)
        time[2] - number of minutes (optional)
        time[3] - number of seconds (optional)
    :return: int, total number of seconds

    Examples:
        calculateTotalSeconds([1, 2, 3, 4]) returns 93784
        calculateTotalSeconds([0, 2, 3]) returns 7380
    */

    var days = time[0] || 0;
    var hours = time[1] || 0;
    var minutes = time[2] || 0;
    var seconds = time[3] || 0;

    return ((days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds);
}