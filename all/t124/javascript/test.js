describe('shuffle function tests', () => {
    test('shuffles an array of numbers', () => {
        const array = [1, 2, 3, 4, 5];
        const shuffledArray = shuffle([...array]);
        expect(shuffledArray.length).toEqual(array.length);
        expect(shuffledArray.every(item => array.includes(item))).toBeTruthy();
        expect(new Set(shuffledArray).size).toEqual(new Set(array).size); // Ensure no duplicates
    });

    test('shuffles an array of strings', () => {
        const array = ["apple", "banana", "cherry", "date", "elderberry"];
        const shuffledArray = shuffle([...array]);
        expect(shuffledArray.length).toEqual(array.length);
        expect(shuffledArray.every(item => array.includes(item))).toBeTruthy();
    });

    test('shuffles an array with duplicate elements', () => {
        const array = [1, 1, 2, 2, 3, 3];
        const shuffledArray = shuffle([...array]);
        expect(shuffledArray.length).toEqual(array.length);
        expect(shuffledArray.every(item => array.includes(item))).toBeTruthy();
    });

    test('shuffles an array with a single element', () => {
        const array = [42];
        const shuffledArray = shuffle([...array]);
        expect(shuffledArray).toEqual(array);
    });

    test('shuffles an empty array', () => {
        const array = [];
        const shuffledArray = shuffle([...array]);
        expect(shuffledArray.length).toEqual(0);
    });
});