function getCurrentDate() {
    // Get the current date
    const now = new Date();

    // Format the date as "YYYY-MM-DD"
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are 0-based
    const day = String(now.getDate()).padStart(2, '0');

    // Return the formatted date string
    return `${year}-${month}-${day}`;
}