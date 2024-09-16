describe('hslToRgb', () => {

    // 基本逻辑功能测试：将 HSL(0, 100%, 50%) 转换为 RGB(255, 0, 0)
    test('should convert HSL(0, 100%, 50%) to RGB(255, 0, 0)', () => {
        const hue = 0;
        const saturation = 100;
        const lightness = 50;
        const expectedOutput = { r: 255, g: 0, b: 0 };
        expect(hslToRgb(hue, saturation, lightness)).toEqual(expectedOutput);
    });

    // 边界值功能测试：将 HSL(360, 100%, 50%) 转换为 RGB(255, 0, 0)
    test('should handle hue of 360 degrees correctly as RGB(255, 0, 0)', () => {
        const hue = 360;
        const saturation = 100;
        const lightness = 50;
        const expectedOutput = { r: 255, g: 0, b: 0 };
        expect(hslToRgb(hue, saturation, lightness)).toEqual(expectedOutput);
    });

    // 边界值功能测试：将 HSL(120, 100%, 50%) 转换为 RGB(0, 255, 0)
    test('should convert HSL(120, 100%, 50%) to RGB(0, 255, 0)', () => {
        const hue = 120;
        const saturation = 100;
        const lightness = 50;
        const expectedOutput = { r: 0, g: 255, b: 0 };
        expect(hslToRgb(hue, saturation, lightness)).toEqual(expectedOutput);
    });

    // 异常值测试：将 HSL(-30, 100%, 50%) 转换为正常范围内的 RGB 值
    test('should handle negative hue values correctly and convert HSL(-30, 100%, 50%) to RGB(255, 85, 0)', () => {
        const hue = -30;
        const saturation = 100;
        const lightness = 50;
        const expectedOutput = { r: 255, g: 0, b: 128 };
        expect(hslToRgb(hue, saturation, lightness)).toEqual(expectedOutput);
    });

    // 异常值测试：当饱和度和亮度为 0 时应输出灰度色 RGB(128, 128, 128)
    test('should return a grayscale color RGB(128, 128, 128) when saturation and lightness are both 0', () => {
        const hue = 120;
        const saturation = 0;
        const lightness = 50;
        const expectedOutput = { r: 128, g: 128, b: 128 };
        expect(hslToRgb(hue, saturation, lightness)).toEqual(expectedOutput);
    });

});
