import { isEqual } from 'lodash';

/**
 * Finds and returns the element from the given array that is closest to the specified target value.
 * If two elements are equally close, the first one encountered is returned.
 *
 * @param target - The target number to which we want to find the closest element.
 * @param elements - An array of numerical elements from which the closest element is to be found.
 * @returns The element from the array that is closest to the target value.
 */
function findClosestElement(target: number, elements: number[]): number {
    let closestElement = elements[0];
    let closestDistance = Math.abs(target - closestElement);

    for (const element of elements) {
        const distance = Math.abs(target - element);
        if (distance < closestDistance) {
            closestElement = element;
            closestDistance = distance;
        }
    }

    return closestElement;
}
describe('TestFindClosestElement', () => {
  it('should return 3 as it is the first closest element to 5', () => {
    expect(findClosestElement(5, [1, 3, 7, 8, 9])).toBe(3);
  });

  it('should return 7 as it exactly matches the target', () => {
    expect(findClosestElement(7, [1, 3, 7, 8, 9])).toBe(7);
  });

  it('should return 4 as it is the first closest element to 5', () => {
    expect(findClosestElement(5, [4, 6, 8, 9])).toBe(4);
  });

  it('should return 3.3 as it is the first closest element to 5.5', () => {
    expect(findClosestElement(5.5, [1.1, 3.3, 7.7, 8.8])).toBe(3.3);
  });
});
