import { convertToCommaSeparated } from './yourModuleName';  // Adjust the import to match your module

describe('convertToCommaSeparated', () => {
    test('basic separators', () => {
        expect(convertToCommaSeparated("apple;banana*orange/mango")).toBe("apple,banana,orange,mango");
    });

    test('mixed separators', () => {
        expect(convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    test('no separators', () => {
        expect(convertToCommaSeparated("watermelon")).toBe("watermelon");
    });

    test('repeated separators', () => {
        expect(convertToCommaSeparated("pear;;apple**banana//orange")).toBe("pear,,apple,,banana,,orange");
    });
});