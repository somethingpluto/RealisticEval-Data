import { isEqual } from 'lodash';

function generateUniquePairs<T>(array: T[]): [T, T][] {
  const pairs: [T, T][] = [];
  const seen: Set<string> = new Set();

  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      const pair = [array[i], array[j]];
      const pairStr = pair.toString();
      if (!seen.has(pairStr)) {
        pairs.push(pair);
        seen.add(pairStr);
      }
    }
  }

  return pairs;
}
describe('generateUniquePairs', () => {
    test('generates unique pairs from an array with three elements', () => {
        const items: string[] = ['A', 'B', 'C'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            ['A', 'B'],
            ['A', 'C'],
            ['B', 'C']
        ]);
    });

    test('generates unique pairs from an array with two elements', () => {
        const items: string[] = ['A', 'B'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([['A', 'B']]);
    });

    test('returns an empty array when the input array is empty', () => {
        const items: string[] = [];
        const result = generateUniquePairs(items);
        expect(result).toEqual([]);
    });

    test('returns an empty array when the input array has one element', () => {
        const items: string[] = ['A'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([]);
    });

    test('handles an array with different types of elements', () => {
        const items: (string | number | { key: string })[] = [1, 'A', { key: 'value' }];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            [1, 'A'],
            [1, { key: 'value' }],
            ['A', { key: 'value' }]
        ]);
    });

    test('generates pairs from an array with more than three elements', () => {
        const items: string[] = ['A', 'B', 'C', 'D'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['B', 'C'],
            ['B', 'D'],
            ['C', 'D']
        ]);
    });
});
