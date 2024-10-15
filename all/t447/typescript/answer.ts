function calculateAge(birthDateString: string): number | string {
    // Parse the birth date string into a Date object
    const birthDate = new Date(birthDateString);
    if (isNaN(birthDate.getTime())) {
        return "Invalid date format. Please enter a valid date.";
    }

    // Get the current date
    const today = new Date();

    // Calculate the age
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDifference = today.getMonth() - birthDate.getMonth();

    // Adjust age if the current month is before the birth month
    // or if it's the birth month and the current date is before the birth date
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    return age;
}