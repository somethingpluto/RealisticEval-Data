// Function to update the clock display
function updateClock() {
    let currentTime = new Date().getTime();
    let elapsedTime = currentTime - startTime;

    let minutes = Math.floor(elapsedTime / 60000);
    let seconds = Math.floor((elapsedTime % 60000) / 1000);

    // Add leading zeros if necessary
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    // Update the clock display
    clockElement.textContent = minutes + ':' + seconds;
}
  