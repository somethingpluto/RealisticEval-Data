describe('TestCamelToSnake', () => {
    it('test basic CamelCase to snake_case conversion', () => {
        expect(camelToSnake("HelloWorld")).toBe("hello_world");
    });

    it('test conversion of a CamelCase string with multiple words', () => {
        expect(camelToSnake("ThisIsATest")).toBe("this_is_a_test");
    });

    it('test conversion with numbers in the string', () => {
        expect(camelToSnake("ConvertThis123String")).toBe("convert_this123_string");
    });

    it('test conversion with leading uppercase letters', () => {
        expect(camelToSnake("PythonFunction")).toBe("python_function");
    });

    it('test conversion of an empty string', () => {
        expect(camelToSnake("")).toBe("");
    });
});