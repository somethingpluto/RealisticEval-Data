describe('isCompliantIP', () => {
    it('should return true for valid IP addresses', () => {
        expect(isCompliantIP('192.168.1.1')).toBe(true);
        expect(isCompliantIP('10.0.0.1')).toBe(true);
        expect(isCompliantIP('172.16.0.1')).toBe(true);
        expect(isCompliantIP('127.0.0.1')).toBe(true);
    });

    it('should return false for invalid IP addresses', () => {
        expect(isCompliantIP('256.256.256.256')).toBe(false); // Out of range
        expect(isCompliantIP('255.255.255.256')).toBe(false); // Out of range
        expect(isCompliantIP('255.255.255.255.1')).toBe(false); // Invalid number of octets
        expect(isCompliantIP('192.168.1')).toBe(false); // Invalid number of octets
        expect(isCompliantIP('192.168.1.a')).toBe(false); // Non-numeric character
        expect(isCompliantIP('192.168.-1.1')).toBe(false); // Negative number
        expect(isCompliantIP('192.168.256.1')).toBe(false); // Out of range
    });
});