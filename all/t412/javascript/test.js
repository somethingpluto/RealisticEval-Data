describe('String Methods', () => {
    describe('#toUpperCase()', () => {
        it('should return the string in uppercase', () => {
            assert.strictEqual('foo'.toUpperCase(), 'FOO');
        });
    });

    describe('#isUpper()', () => {
        it('should return true if the string is in uppercase', () => {
            assert.strictEqual('FOO'.isUpper(), true);
        });
        
        it('should return false if the string is not in uppercase', () => {
            assert.strictEqual('Foo'.isUpper(), false);
        });
    });

    describe('#split()', () => {
        it('should split the string into an array of words', () => {
            const s = 'hello world';
            assert.deepStrictEqual(s.split(), ['hello', 'world']);
        });

        it('should throw TypeError when called with non-integer argument', () => {
            const s = 'hello world';
            assert.throws(() => s.split(2), TypeError);
        });
    });
});