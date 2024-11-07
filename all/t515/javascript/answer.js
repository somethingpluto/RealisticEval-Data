function formatDateString(dateStr) {
    try {
        // Convert to a Date object using the specified format
        const dateObject = new Date(dateStr);

        // Check if the date is valid
        if (isNaN(dateObject)) {
            console.log("Error parsing date: Invalid date string");
            return null;
        }

        // Extract components of the date
        const year = dateObject.getUTCFullYear();
        const month = String(dateObject.getUTCMonth() + 1).padStart(2, '0');
        const day = String(dateObject.getUTCDate()).padStart(2, '0');
        const hours = String(dateObject.getUTCHours()).padStart(2, '0');
        const minutes = String(dateObject.getUTCMinutes()).padStart(2, '0');
        const seconds = String(dateObject.getUTCSeconds()).padStart(2, '0');

        // Format the date string
        const formattedDate = `${year}-${month}-${day}_${hours}:${minutes}:${seconds}`;

        return formattedDate;
    } catch (error) {
        console.log(`Error parsing date: ${error}`);
        return null;
    }
}