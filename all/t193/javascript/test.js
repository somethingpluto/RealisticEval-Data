describe('convFlags Test Cases', () => {
    test('convFlags(0x0000001F)', () => {
        expect(convFlags(0x0000001F)).toBe("FFFFFFE0");
    });

    test('convFlags(0x00000015)', () => {
        expect(convFlags(0x00000015)).toBe("FFFFFFEA");
    });

    test('convFlags(0xFFFFFFFF)', () => {
        expect(convFlags(0xFFFFFFFF)).toBe("0");
    });

    test('convFlags(0x12345678)', () => {
        expect(convFlags(0x12345678)).toBe("EDCBA987");
    });

    test('convFlags(0x00000001)', () => {
        expect(convFlags(0x00000001)).toBe("FFFFFFFE");
    });

    test('convFlags(0x00000003)', () => {
        expect(convFlags(0x00000003)).toBe("FFFFFFFC");
    });

    test('convFlags(0x00000008)', () => {
        expect(convFlags(0x00000008)).toBe("FFFFFFF7");
    });

    test('convFlags(0xABCDEF01)', () => {
        expect(convFlags(0xABCDEF01)).toBe("543210FE");
    });
});