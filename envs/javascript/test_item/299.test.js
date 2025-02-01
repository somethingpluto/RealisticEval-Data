/**
 * Calculates the age from the given birth date string and returns a string containing the original birth date and the calculated age. If the entered date string is invalid or empty, the function returns an empty string.
 *
 * @param {string} birthDateString - The birth date as a string in a recognizable date format (e.g., 'YYYY-MM-DD').
 * @returns {string} - A string that includes the original birth date and the calculated age in the format 'birthDateString (age)', or an empty string if the input is invalid.
 */
function calculateAge(birthDateString) {
    if (!birthDateString) {
        return '';
    }

    const birthDate = new Date(birthDateString);
    if (isNaN(birthDate.getTime())) {
        return '';
    }

    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    return `${birthDateString} (${age})`;
}
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

