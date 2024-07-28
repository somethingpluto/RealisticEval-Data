int getDaysInMonth(int year, int month)
{

    // Adjust February for leap years
    if (month == 2)
    {
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        {
            return 29; // Leap year
        }
        else
        {
            return 28; // Non-leap year
        }
    }

    return daysInMonth[month];
}