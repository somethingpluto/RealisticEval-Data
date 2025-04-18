function getTimeSinceBornUntilNow(birthDate) {
    const now = new Date();

    // Calculate years
    let years = now.getFullYear() - birthDate.getFullYear();

    // Calculate months
    let months = now.getMonth() - birthDate.getMonth();
    if (months < 0) {
        years -= 1;
        months += 12;
    }

    // Calculate days
    let days = now.getDate() - birthDate.getDate();
    if (days < 0) {
        months -= 1;
        const previousMonth = new Date(now.getFullYear(), now.getMonth(), 0);
        days += previousMonth.getDate();
    }

    // Calculate hours
    let hours = now.getHours() - birthDate.getHours();
    if (hours < 0) {
        days -= 1;
        hours += 24;
    }

    // Calculate minutes
    let minutes = now.getMinutes() - birthDate.getMinutes();
    if (minutes < 0) {
        hours -= 1;
        minutes += 60;
    }

    return [years, months, days, hours, minutes];
}