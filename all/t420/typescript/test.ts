describe('TestGetMinDistance', () => {
    beforeEach(() => {
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => '');
    });

    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('should handle a simple case', () => {
        const mockFileContent = [
            "hello world",
            "hello hello world",
            "world hello"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });

    it('should handle multiple lines', () => {
        const mockFileContent = [
            "hello planet",
            "world hello planet",
            "hello world planet"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([1, 1]);
    });

    it('should handle large distances', () => {
        const mockFileContent = [
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 27]);
    });

    it('should handle adjacent words', () => {
        const mockFileContent = [
            "hello world",
            "hello hello world world",
            "world hello"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });
});