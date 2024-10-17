describe('TestStrongPassword', () => {
    it('should validate a strong password that meets all criteria', () => {
        expect(isStrongPassword("StrongPass1")).toBe(true);
    });

    it('should fail a password missing a lowercase letter', () => {
        expect(isStrongPassword("STRONGPASS1")).toBe(false);
    });

    it('should fail a password missing an uppercase letter', () => {
        expect(isStrongPassword("strongpass1")).toBe(false);
    });

    it('should fail a password missing a number', () => {
        expect(isStrongPassword("StrongPassword")).toBe(false);
    });

    it('should fail a password that is too short', () => {
        expect(isStrongPassword("Short1")).toBe(false);
    });

    it('should validate a password that includes special characters but is still strong', () => {
        expect(isStrongPassword("Strong!Password1")).toBe(true);
    });
});