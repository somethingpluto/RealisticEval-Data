// ... (previous code for context)

function generateCombinations<T>(inputLists: Array<Array<T>>): Array<Array<T>> {
  if (inputLists.length === 0) {
    return [];
  }

  const result: Array<Array<T>> = [];
  const combinations = generateCombinationsHelper(inputLists, 0, []);

  return result.concat(combinations);
}

function generateCombinationsHelper<T>(
  lists: Array<Array<T>>,
  index: number,
  currentCombination: Array<T>
): Array<Array<T>> {
  if (index === lists.length) {
    return [currentCombination];
  }

  const currentList = lists[index];
  const combinations: Array<Array<T>> = [];

  for (const element of currentList) {
    const newCombination = [...currentCombination, element];
    combinations.push(...generateCombinationsHelper(lists, index + 1, newCombination));
  }

  return combinations;
}

// ... (rest of the code)
describe('generateCombinations', () => {
    
    test('should return an empty array for empty input', () => {
        const inputData: Array<Array<string>> = [];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return an empty array for a single empty list', () => {
        const inputData: Array<Array<string>> = [[]];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return combinations for a single non-empty list', () => {
        const inputData: Array<Array<string>> = [['a', 'b', 'c']];
        const expected: Array<Array<string>> = [['a'], ['b'], ['c']];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return combinations for multiple lists', () => {
        const inputData: Array<Array<string>> = [['a', 'b'], ['1', '2']];
        const expected: Array<Array<string>> = [['a', '1'], ['a', '2'], ['b', '1'], ['b', '2']];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return an empty array for input containing an empty list', () => {
        const inputData: Array<Array<string>> = [['a', 'b'], [], ['1', '2']];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

});
