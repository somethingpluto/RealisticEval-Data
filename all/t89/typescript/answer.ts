function timePassed(startTimeInMillis: number): string {
    // Get the current time in milliseconds
    const currentTimeInMillis: number = Date.now();

    // Calculate the difference in milliseconds
    const timeDifference: number = currentTimeInMillis - startTimeInMillis;

    // Convert the difference to seconds
    const totalSeconds: number = Math.floor(timeDifference / 1000);

    // Calculate minutes and seconds
    const minutes: number = Math.floor(totalSeconds / 60);
    const seconds: number = totalSeconds % 60;

    // Return the formatted string
    return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}