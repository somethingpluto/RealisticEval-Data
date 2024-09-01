describe('setEurValue', () => {
    test('Birthday today, should be 24 years old', () => {
        expect(calculateAge('2000-08-23')).toBe('2000-08-23 (24)')
    });

    test('Birthday has passed this year, should be 34 years old', () => {
        expect(calculateAge('1990-01-15')).toBe('1990-01-15 (34)')
    });

    test('Birthday at the end of the year, should be 38 years old', () => {
        expect(calculateAge('1985-12-31')).toBe('1985-12-31 (38)')
    });

    test('Recently turned 1 year old this year', () => {
        expect(calculateAge('2023-05-05')).toBe('2023-05-05 (1)')
    });


    test('Invalid date input should return an empty string', () => {
        expect(calculateAge('invalid-date')).toBe('')
    });
});

/* function created using chatGPT */
function calculateAge(birthDateString) {
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
