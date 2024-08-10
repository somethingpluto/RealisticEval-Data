int days_in_month(int month, int year) {
    switch (month) {
        case 1: return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) ? 29 : 28; // February
        case 3: case 5: case 8: case 10: return 30; // April, June, September, November
        default: return 31; // January, March, May, July, August, October, December
    }
}
