function dayOfWeek(year: number, month: number, day: number): number {
    const t: number[] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    if (month < 3) {
        year -= 1;
    }
    const result = (year + Math.floor(year / 4) - Math.floor(year / 100) + Math.floor(year / 400) + t[month - 1] + day) % 7;
    return (result === 0) ? 7 : (result % 7); // Adjusted to correctly map Sunday as 7
}