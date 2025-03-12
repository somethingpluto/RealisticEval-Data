import { isStrongPassword } from './passwordValidator';

describe('isStrongPassword', () => {
  it('should return true for a strong password', () => {
    expect(isStrongPassword('Str0ngP@ss')).toBeTruthy();
  });

  it('should return false for a password without lowercase letters', () => {
    expect(isStrongPassword('STR0NG')).toBeFalsy();
  });

  it('should return false for a password without uppercase letters', () => {
    expect(isStrongPassword('strong1')).toBeFalsy();
  });

  it('should return false for a password without numbers', () => {
    expect(isStrongPassword('StrongPass')).toBeFalsy();
  });

  it('should return false for a password shorter than 8 characters', () => {
    expect(isStrongPassword('Strong1')).toBeFalsy();
  });

  it('should return true for a password that meets all criteria', () => {
    expect(isStrongPassword('Str0ngP@ss123')).toBeTruthy();
  });
});
describe('TestStrongPassword', () => {
  it('test valid password', () => {
    // Test a strong password that meets all criteria.
    expect(isStrongPassword("StrongPass1")).toBe(true);
  });

  it('test missing lowercase', () => {
    // Test a password missing a lowercase letter.
    expect(isStrongPassword("STRONGPASS1")).toBe(false);
  });

  it('test missing uppercase', () => {
    // Test a password missing an uppercase letter.
    expect(isStrongPassword("strongpass1")).toBe(false);
  });

  it('test missing number', () => {
    // Test a password missing a number.
    expect(isStrongPassword("StrongPassword")).toBe(false);
  });

  it('test too short', () => {
    // Test a password that is too short.
    expect(isStrongPassword("Short1")).toBe(false);
  });

  it('test valid with special characters', () => {
    // Test a password that includes special characters but is still strong.
    expect(isStrongPassword("Strong!Password1")).toBe(true);
  });
});
