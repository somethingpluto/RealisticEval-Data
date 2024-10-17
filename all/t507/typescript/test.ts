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