describe('TestHandleNestedData', () => {
    describe('test_simple_dictionary', () => {
        it('should correctly handle a simple dictionary', () => {
            const data = { name: Buffer.from('Alice'), age: '30' };
            const expected = { name: 'Alice', age: 30 };
            expect(handleNestedData(data)).toEqual(expected);
        });
    });

    describe('test_nested_dictionary', () => {
        it('should correctly handle a nested dictionary', () => {
            const data = { user: { name: Buffer.from('Bob'), details: { age: '25', height: '175.5' } } };
            const expected = { user: { name: 'Bob', details: { age: 25, height: 175.5 } } };
            expect(handleNestedData(data)).toEqual(expected);
        });
    });

    describe('test_list_of_mixed_data_types', () => {
        it('should correctly handle a list of mixed data types', () => {
            const data = ['100', Buffer.from('200'), 300.0, '400.5'];
            const expected = [100, '200', 300.0, 400.5];
            expect(handleNestedData(data)).toEqual(expected);
        });
    });

    describe('test_incorrect_byte_decoding', () => {
        it('should throw an error when decoding invalid bytes', () => {
            const data = { invalid_bytes: Buffer.from('\xff\xfe\xfd\xfc') };
            expect(() => handleNestedData(data)).toThrow(/UnicodeDecodeError/);
        });
    });

    describe('test_complex_nested_structure', () => {
        it('should correctly handle a complex nested structure', () => {
            const data = {
                team: [
                    { name: Buffer.from('Charlie'), scores: ['1000', '2000.2'] },
                    { name: Buffer.from('Daisy'), skills: [Buffer.from('Coding'), 'Design'], age: '22' }
                ]
            };
            const expected = {
                team: [
                    { name: 'Charlie', scores: [1000, 2000.2] },
                    { name: 'Daisy', skills: ['Coding', 'Design'], age: 22 }
                ]
            };
            expect(handleNestedData(data)).toEqual(expected);
        });
    });
});