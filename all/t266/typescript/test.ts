describe('TestHandleNestedData', () => {
    it('test simple dictionary', () => {
        const data = { name: b"Alice", age: "30" };
        const expected = { name: "Alice", age: 30 };
        expect(handleNestedData(data)).toEqual(expected);
    });

    it('test nested dictionary', () => {
        const data = { user: { name: b"Bob", details: { age: "25", height: "175.5" } } };
        const expected = { user: { name: "Bob", details: { age: 25, height: 175.5 } } };
        expect(handleNestedData(data)).toEqual(expected);
    });

    it('test list of mixed data types', () => {
        const data = ["100", b"200", 300.0, "400.5"];
        const expected = [100, "200", 300.0, 400.5];
        expect(handleNestedData(data)).toEqual(expected);
    });

    it('test incorrect byte decoding', () => {
        const data = { invalid_bytes: b"\xff\xfe\xfd\xfc" };
        expect(() => handleNestedData(data)).toThrow(/UnicodeDecodeError/);
    });

    it('test complex nested structure', () => {
        const data = {
            team: [
                { name: b"Charlie", scores: ["1000", "2000.2"] },
                { name: b"Daisy", skills: [b"Coding", "Design"], age: "22" }
            ]
        };
        const expected = {
            team: [
                { name: "Charlie", scores: [1000, 2000.2] },
                { name: "Daisy", skills: ["Coding", "Design"], age: 22 }
            ]
        };
        expect(handleNestedData(data)).toEqual(expected);
    });
});