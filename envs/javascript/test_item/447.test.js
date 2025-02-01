/**
 * Calculate age based on the birth date string entered by the user.Input birthDateString format such as 2000-01-01
 * @param {string} birthDateString
 * @returns {string|number}
 */
function calculateAge(birthDateString) {
    const birthDate = new Date(birthDateString);
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}
describe('calculateAge', () => {
    test('calculates age correctly for a birth date in the past', () => {
        expect(calculateAge('2000-01-01')).toBe(new Date().getFullYear() - 2000);
    });

    test('calculates age correctly for a birth date in the long past', () => {
        expect(calculateAge('1000-01-01')).toBe(new Date().getFullYear() - 1000);
    });


    test('calculates age correctly for a birth date today', () => {
        const today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
        expect(calculateAge(today)).toBe(0);
    });


    test('calculates age correctly for a person born yesterday', () => {
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1); // Set to yesterday
        const birthDateString = yesterday.toISOString().split('T')[0];
        expect(calculateAge(birthDateString)).toBe(0);
    });
});

