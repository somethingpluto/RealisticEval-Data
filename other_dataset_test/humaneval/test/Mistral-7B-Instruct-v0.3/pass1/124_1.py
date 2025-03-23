def check(candidate):

    # Check some simple cases
    assert candidate('03-11-2000') == True

    assert candidate('15-01-2012') == False

    assert candidate('04-0-2040') == False

    assert candidate('06-04-2020') == True

    assert candidate('01-01-2007') == True

    assert candidate('03-32-2011') == False

    assert candidate('') == False

    assert candidate('04-31-3000') == False

    assert candidate('06-06-2005') == True

    assert candidate('21-31-2000') == False

    assert candidate('04-12-2003') == True

    assert candidate('04122003') == False

    assert candidate('20030412') == False

    assert candidate('2003-04') == False

    assert candidate('2003-04-12') == False

    assert candidate('04-2003') == False
def valid_date(date):
    try:
        month, day, year = map(int, date.split('-'))
        if len(date)!= 10 or month < 1 or month > 12 or day < 1 or day > 31:
            if month == 2 and day > 29:
                return False
            if (month in [4, 6, 9, 11] and day > 30) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31):
                return False
        return True
    except ValueError:
        return False
candidate = valid_date
check(candidate)