// Function to update the clock display by calculating the elapsed time since a given start time
function getMinuteAndSecondSinceTime(startTime) {
    // Get the current time in milliseconds
    const currentTime = new Date().getTime();

    // Calculate the elapsed time in milliseconds
    const elapsedTime = currentTime - startTime;

    // Convert elapsed time to minutes and seconds
    let minutes = Math.floor(elapsedTime / 60000); // 60000 ms in 1 minute
    let seconds = Math.floor((elapsedTime % 60000) / 1000); // Remaining milliseconds converted to seconds

    // Add leading zeros to minutes and seconds if they are less than 10
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;

    // Return the formatted time string in mm:ss format
    return minutes + ":" + seconds;
}