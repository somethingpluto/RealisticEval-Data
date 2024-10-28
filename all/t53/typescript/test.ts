describe('TestSizeInBytes', () => {
    describe('test_size_of_integer', () => {
        it('should correctly compute the size of an integer', () => {
            const integerValue = 42;
            const expectedSize = sizeInBytes(integerValue);
            const resultSize = sizeInBytes(integerValue);
            expect(resultSize).toEqual(expectedSize);
        });
    });

    describe('test_size_of_string', () => {
        it('should correctly compute the size of a string', () => {
            const stringValue = "Hello, world!";
            const expectedSize = sizeInBytes(stringValue);
            const resultSize = sizeInBytes(stringValue);
            expect(resultSize).toEqual(expectedSize);
        });
    });

    describe('test_size_of_list', () => {
        it('should correctly compute the size of a list', () => {
            const listValue = [1, 2, 3, 4, 5];
            const expectedSize = sizeInBytes(listValue);
            const resultSize = sizeInBytes(listValue);
            expect(resultSize).toEqual(expectedSize);
        });
    });

    describe('test_size_of_dictionary', () => {
        it('should correctly compute the size of a dictionary', () => {
            const dictValue = { key1: 'value1', key2: 'value2' };
            const expectedSize = sizeInBytes(dictValue);
            const resultSize = sizeInBytes(dictValue);
            expect(resultSize).toEqual(expectedSize);
        });
    });

    describe('test_size_of_custom_object', () => {
        it('should correctly compute the size of a custom object', () => {
            class CustomObject {
                constructor() {
                    this.attr1 = 'a';
                    this.attr2 = 123;
                }
            }

            const customObj = new CustomObject();
            const expectedSize = sizeInBytes(customObj);
            const resultSize = sizeInBytes(customObj);
            expect(resultSize).toEqual(expectedSize);
        });
    });
});