function calculateAge(birthDateString: string): string {
    if (!birthDateString || isNaN(Date.parse(birthDateString))) {
        return '';
    }

    const today = new Date();
    const birthDate = new Date(birthDateString);
    let age = today.getFullYear() - birthDate.getFullYear();

    const isBirthdayPassed = today.getMonth() > birthDate.getMonth() ||
        (today.getMonth() === birthDate.getMonth() && today.getDate() >= birthDate.getDate());

    if (!isBirthdayPassed) {
        age--;
    }

    return `${birthDateString} (${age})`;
}