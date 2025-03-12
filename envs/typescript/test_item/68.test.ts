import { List } from 'immutable';

function divideList(lst: List<number>, n: number): List<List<number>> {
    if (n <= 0) {
        throw new Error('Number of parts must be greater than 0');
    }
    if (lst.isEmpty()) {
        return List.of(List.of()).take(n);
    }
    const size = Math.ceil(lst.size / n);
    const divided = lst.partition(size);
    return divided[0].concat(divided[1].take(size - divided[0].size)).toList();
}
describe('TestDivideList', () => {
  it('should handle even division', () => {
    const lst = [1, 2, 3, 4, 5, 6];
    const n = 3;
    const expected = [[1, 2], [3, 4], [5, 6]];
    expect(divideList(lst, n)).toEqual(expected);
  });

  it('should handle uneven division', () => {
    const lst = [1, 2, 3, 4, 5, 6, 7];
    const n = 3;
    const expected = [[1, 2, 3], [4, 5], [6, 7]];
    expect(divideList(lst, n)).toEqual(expected);
  });

  it('should handle more parts than items', () => {
    const lst = [1, 2, 3];
    const n = 5;
    const expected = [[1], [2], [3], [], []];
    expect(divideList(lst, n)).toEqual(expected);
  });

  it('should handle a single element', () => {
    const lst = [1];
    const n = 1;
    const expected = [[1]];
    expect(divideList(lst, n)).toEqual(expected);
  });

  it('should handle an empty list', () => {
    const lst: number[] = [];
    const n = 3;
    const expected = [[], [], []];
    expect(divideList(lst, n)).toEqual(expected);
  });
});
