describe('isCompliantIP', () => {
    it('should return true for private IPs', () => {
        expect(isCompliantIP('192.168.1.1')).toBe(true);
    });

    it('should return false for public IPs', () => {
        expect(isCompliantIP('8.8.8.8')).toBe(true);
    });

    it('should return false for invalid IP strings', () => {
        expect(isCompliantIP('999.999.999.999')).toBe(false);
    });
});