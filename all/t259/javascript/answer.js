function isCompliantFourDigit(number) {
    return Number.isInteger(number) && number >= 1000 && number <= 9999;
}