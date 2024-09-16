function timePassed(startTimeInMillis) {
    // Get the current time in milliseconds
    const currentTimeInMillis = Date.now();

    // Calculate the difference in milliseconds
    const timeDifference = currentTimeInMillis - startTimeInMillis;

    // Convert the difference to seconds
    const totalSeconds = Math.floor(timeDifference / 1000);

    // Calculate minutes and seconds
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;

    // Return the formatted string
    return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}