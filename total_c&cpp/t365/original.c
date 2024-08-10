int day_of_week(int day, int month, int year) {
    struct tm time_in = { 0, 0, 0, day, month, year - 1900 };
    time_t time_temp = mktime(&time_in);

    // Extract day of the week (0=Sunday, 1=Monday, ..., 6=Saturday)
    struct tm *time_out = localtime(&time_temp);
    return time_out->tm_wday;
}
