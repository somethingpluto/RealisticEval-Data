function getTimeDifference(date) {
    // Get the current date
    const currentDate = new Date();

    // Calculate the time difference in milliseconds
    const differenceInMilliseconds = currentDate - new Date(date);

    // Convert the time difference to days, hours, and minutes
    const totalMinutes = Math.floor(differenceInMilliseconds / (1000 * 60));
    const days = Math.floor(totalMinutes / (60 * 24));
    const hours = Math.floor((totalMinutes % (60 * 24)) / 60);
    const minutes = totalMinutes % 60;

    // Return the formatted string
    return `Day: ${days} Hour: ${hours} Minutes: ${minutes}`;
}
