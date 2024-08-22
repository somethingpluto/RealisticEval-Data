describe('getObjectById', () => {

    test('should return the object with the matching id', () => {
        const list = [
            { id: 1, name: 'Object 1' },
            { id: 2, name: 'Object 2' },
            { id: 3, name: 'Object 3' }
        ];
        const result = getObjectById(2, list);
        expect(result).toEqual({ id: 2, name: 'Object 2' });
    });

    test('should return null if no object with the matching id is found', () => {
        const list = [
            { id: 1, name: 'Object 1' },
            { id: 2, name: 'Object 2' },
            { id: 3, name: 'Object 3' }
        ];
        const result = getObjectById(4, list);
        expect(result).toBeNull();
    });

    test('should return null if the list is empty', () => {
        const list = [];
        const result = getObjectById(1, list);
        expect(result).toBeNull();
    });

    test('should return null if objects in the list do not have an id property', () => {
        const list = [
            { name: 'Object 1' },
            { name: 'Object 2' },
            { name: 'Object 3' }
        ];
        const result = getObjectById(1, list);
        expect(result).toBeNull();
    });

    test('should return the correct object when id is a string', () => {
        const list = [
            { id: 'a', name: 'Object A' },
            { id: 'b', name: 'Object B' },
            { id: 'c', name: 'Object C' }
        ];
        const result = getObjectById('b', list);
        expect(result).toEqual({ id: 'b', name: 'Object B' });
    });

});