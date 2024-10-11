describe('method_arg_type_check', () => {
    test('should pass when arguments match expected types', () => {
        const method = (str: string, num: number) => {};
        method_arg_type_check(method, 'test', 42);
    });

    test('should fail when an argument does not match the expected type', () => {
        const method = (str: string, num: number) => {};
        expect(() => method_arg_type_check(method, 'test', 'not a number')).toThrowError('Argument \'num\' must be of type number, but got string');
    });

    test('should handle optional parameters correctly', () => {
        const method = (str: string, num?: number) => {};
        method_arg_type_check(method, 'test'); // Should pass
        method_arg_type_check(method, 'test', 42); // Should also pass
    });
});