import { v4 as uuidv4 } from 'uuid';

function generateUniqueId(): string {
  return uuidv4();
}

function addObjectToList(uniqueId: string, list: Array<Record<string, any>>): void {
  list.push({ id: uniqueId, data: {} });
}

// ... (rest of the previous code)

function updateObjectData(id: string | number, newData: Record<string, any>, list: Array<Record<string, any>>): void {
  const objectToUpdate = getObjectById(id, list);
  if (objectToUpdate) {
    Object.assign(objectToUpdate.data, newData);
  }
}

function removeObjectById(id: string | number, list: Array<Record<string, any>>): void {
  const index = list.findIndex(item => item.id === id);
  if (index !== -1) {
    list.splice(index, 1);
  }
}
describe('getObjectById', () => {
    test('should return the object with the matching id', () => {
        const list: Array<{ id: number; name: string }> = [
            { id: 1, name: 'Object 1' },
            { id: 2, name: 'Object 2' },
            { id: 3, name: 'Object 3' }
        ];
        const result = getObjectById(2, list);
        expect(result).toEqual({ id: 2, name: 'Object 2' });
    });

    test('should return null if no object with the matching id is found', () => {
        const list: Array<{ id: number; name: string }> = [
            { id: 1, name: 'Object 1' },
            { id: 2, name: 'Object 2' },
            { id: 3, name: 'Object 3' }
        ];
        const result = getObjectById(4, list);
        expect(result).toBeNull();
    });

    test('should return null if the list is empty', () => {
        const list: Array<{ id: number; name: string }> = [];
        const result = getObjectById(1, list);
        expect(result).toBeNull();
    });

    test('should return null if objects in the list do not have an id property', () => {
        const list: Array<{ name: string }> = [
            { name: 'Object 1' },
            { name: 'Object 2' },
            { name: 'Object 3' }
        ];
        const result = getObjectById(1, list);
        expect(result).toBeNull();
    });

    test('should return the correct object when id is a string', () => {
        const list: Array<{ id: string; name: string }> = [
            { id: 'a', name: 'Object A' },
            { id: 'b', name: 'Object B' },
            { id: 'c', name: 'Object C' }
        ];
        const result = getObjectById('b', list);
        expect(result).toEqual({ id: 'b', name: 'Object B' });
    });
});
