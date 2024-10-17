describe('TestComputeMD5', () => {
    test('test the MD5 hash of an empty string', () => {
        expect(computeMD5('')).toBe('d41d8cd98f00b204e9800998ecf8427e');
    });

    test('test the MD5 hash of a simple string', () => {
        expect(computeMD5('Hello, World!')).toBe('65a8e27d8879283831b664bd8b7f0ad4');
    });

    test('test the MD5 hash of a numeric string', () => {
        expect(computeMD5('123456')).toBe('e10adc3949ba59abbe56e057f20f883e');
    });

    test('test the MD5 hash of a string with special characters', () => {
        expect(computeMD5('!@#$%^&*()')).toBe('05b28d17a7b6e7024b6e5d8cc43a8bf7');
    });

    test('test the MD5 hash of a long string', () => {
        const longString = 'a'.repeat(1000); // A string of 1000 'a' characters
        const expectedHash = 'cabe45dcc9ae5b66ba86600cca6b8ba8'; // MD5 of 'aaaa....' (1000 'a's)
        expect(computeMD5(longString)).toBe(expectedHash);
    });
});