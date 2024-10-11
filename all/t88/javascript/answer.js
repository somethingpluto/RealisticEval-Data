function isCronBetween2And4AM(cronExpression) {
    const parts = cronExpression.split(' ');
    const hourPart = parts[1];

    const hours = hourPart.split(',').map(Number);
    return hours.some(hour => hour >= 2 && hour < 4);
}