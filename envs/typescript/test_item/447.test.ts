import { format, parseISO } from 'date-fns';

function calculateAge(birthDateString: string): string | number {
  const today = new Date();
  const birthDate = parseISO(birthDateString);
  if (isNaN(birthDate.getTime())) {
    return 'Invalid date format. Please use YYYY-MM-DD.';
  }
  if (birthDate > today) {
    return 'Birth date cannot be in the future.';
  }
  const age = today.getFullYear() - birthDate.getFullYear();
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
