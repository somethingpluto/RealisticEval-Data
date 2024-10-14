function isBreakTime(startTime: string, endTime: string, currentTime: string): boolean {
    const [startHour, startMinute] = startTime.split(':').map(Number);
    const [endHour, endMinute] = endTime.split(':').map(Number);
    const [currentHour, currentMinute] = currentTime.split(':').map(Number);

    const startTotalMinutes = startHour * 60 + startMinute;
    const endTotalMinutes = endHour * 60 + endMinute;
    const currentTotalMinutes = currentHour * 60 + currentMinute;

    return currentTotalMinutes >= startTotalMinutes && currentTotalMinutes <= endTotalMinutes;
}