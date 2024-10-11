const sizeInBytes = require('./path-to-your-sizeInBytes-function'); // Adjust with the correct path to where your sizeInBytes function is defined

describe('TestSizeInBytes', () => {

    test('test size of integer', () => {
        const integerValue = 42;
        const expectedSize = (new ArrayBuffer(8)).byteLength; //1 number generally takes 8 bytes
        const resultSize = sizeInBytes(integerValue);
        expect(resultSize).toBe(expectedSize);
    });

    test('test size of string', () => {
        const stringValue = "Hello, world!";
        // JavaScript string size estimation (length of string * 2 bytes per character)
        const expectedSize = stringValue.length * 2;
        const resultSize = sizeInBytes(stringValue);
        expect(resultSize).toBe(expectedSize);
    });

    test('test size of list', () => {
        const listValue = [1, 2, 3, 4, 5];
        // Rough estimation for list, assuming each number is 8 bytes
        const expectedSize = listValue.length * 8;
        const resultSize = sizeInBytes(listValue);
        expect(resultSize).toBe(expectedSize);
    });

    test('test size of dictionary', () => {
        const dictValue = {'key1': 'value1', 'key2': 'value2'};
        // Rough estimation for key-value pairs; val1: length*2, val2: length*2
        let expectedSize = 0;
        for (const key in dictValue) {
            expectedSize += key.length * 2; // key length
            expectedSize += dictValue[key].length * 2; // value length
        }
        const resultSize = sizeInBytes(dictValue);
        expect(resultSize).toBe(expectedSize);
    });

    test('test size of custom object', () => {
        class CustomObject {
            constructor() {
                this.attr1 = 'a';
                this.attr2 = 123;
            }
        }

        const customObj = new CustomObject();
        // Rough estimation for custom object; attr1: length*2, attr2: 8 bytes
        let expectedSize = 'a'.length * 2 + 8;
        const resultSize = sizeInBytes(customObj);
        expect(resultSize).toBe(expectedSize);
    });
});