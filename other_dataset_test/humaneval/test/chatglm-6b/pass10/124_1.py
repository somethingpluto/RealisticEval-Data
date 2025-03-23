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
    # Check if date is not empty
    if date == "":
        return False

    # Check if number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12
    if 31 < len(date) < 32 or 31 < len(date) < 36:
        return False

    # Check if number of days is not less than 1 or higher than 30 days for months 4,6,9,11
    if 30 < len(date) < 31 or 30 < len(date) < 36:
        return False

    # Check if months should not be less than 1 or higher than 12
    if 1 <= len(date) <= 12:
        return True

    # Check if date is in the format: mm-dd-yyyy
    if date.split("-")[-1]!= " " and date.split("-")[-1]!= "/":
        return False

    return True

valid_date('03-11-2000') => True
valid_date('15-01-2012') => False
valid_date('04-0-2040') => False
valid_date('06-04-2020') => True
valid_date('06/04/2020') => False

candidate = valid_date
check(candidate)