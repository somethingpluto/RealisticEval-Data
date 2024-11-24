function formatDateString(dateStr: string): string | null {
    try {
        // Convert to a Date object using the specified format
        const dateObject = new Date(dateStr);

        // Check if the date is valid
        if (isNaN(dateObject.getTime())) {
            console.log("Error parsing date: Invalid date string");
            return null;
        }

        // Extract components of the date
        const year: number = dateObject.getUTCFullYear();
        const month: string = String(dateObject.getUTCMonth() + 1).padStart(2, '0');
        const day: string = String(dateObject.getUTCDate()).padStart(2, '0');
        const hours: string = String(dateObject.getUTCHours()).padStart(2, '0');
        const minutes: string = String(dateObject.getUTCMinutes()).padStart(2, '0');
        const seconds: string = String(dateObject.getUTCSeconds()).padStart(2, '0');

        // Format the date string
        const formattedDate: string = `${year}-${month}-${day}_${hours}:${minutes}:${seconds}`;

        return formattedDate;
    } catch (error) {
        console.log(`Error parsing date: ${error}`);
        return null;
    }
}
