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
function getObjectById(id, list) { // created by ChatGPT
    // Iterate over the list of objects
    for (let i = 0; i < list.length; i++) {
        const obj = list[i];

        // Check if the object has an `id` property that matches the given id
        if (obj.id && obj.id === id) {
            // If a match is found, return the object
            return obj;
        }
    }

    // If no match is found, return null
    return null;
}