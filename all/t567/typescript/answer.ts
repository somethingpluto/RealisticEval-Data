function getRelativeTime(messageDate: Date): string {
    const now = new Date();
    const timeDifference = now.getTime() - messageDate.getTime();

    const oneDay = 1000 * 60 * 60 * 24; // milliseconds in one day
    const daysDifference = Math.floor(timeDifference / oneDay);

    // Check if the message was created today
    if (daysDifference === 0) {
        return "Today";
    }
    // Check if the message was created yesterday
    else if (daysDifference === 1) {
        return "Yesterday";
    }
    // Check if the message was created within the past week (not today or yesterday)
    else if (daysDifference < 7) {
        const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        return daysOfWeek[messageDate.getDay()];
    }
    // If the message was created earlier than one week ago
    else {
        // Format the date to a readable string (e.g., "MM/DD/YYYY")
        const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'numeric', day: 'numeric' };
        return messageDate.toLocaleDateString(undefined, options);
    }
}
