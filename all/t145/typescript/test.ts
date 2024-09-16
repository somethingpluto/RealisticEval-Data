describe('formatCurrency', () => {
    test('should format number as USD currency for en-US locale', () => {
        const result = formatCurrency(1234.56, "USD", "en-US");
        expect(result).toBe("$1,234.56");
    });

    test('should format number as EUR currency for de-DE locale', () => {
        const result = formatCurrency(1234.56, "EUR", "de-DE");
        expect(result).toBe("1.234,56 €"); // Notice the space character, which may appear in some browsers
    });

    test('should format number as JPY currency for ja-JP locale', () => {
        const result = formatCurrency(1234.56, "JPY", "ja-JP");
        expect(result).toBe("￥1,235"); // JPY does not use decimals
    });

    test('should format number as GBP currency for en-GB locale', () => {
        const result = formatCurrency(1234.56, "GBP", "en-GB");
        expect(result).toBe("£1,234.56");
    });

    test('should format number as CNY currency for zh-CN locale', () => {
        const result = formatCurrency(1234.56, "CNY", "zh-CN");
        expect(result).toBe("￥1,234.56");
    });
});