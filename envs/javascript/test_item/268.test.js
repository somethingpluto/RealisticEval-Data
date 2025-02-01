/**
 * Determines if there exists a starting gas station's index where you can travel
 * around the circuit once in a clockwise direction.
 *
 * @param {number[]} gas - List of integers representing the amount of gas at each station.
 * @param {number[]} cost - List of integers representing the cost of gas to travel from each station to the next.
 * @returns {number} The starting gas station's index if the circuit can be completed, otherwise -1.
 */
function canCompleteCircuit(gas, cost) {
    let totalGas = 0;
    let totalCost = 0;
    let start = 0;
    let gasTank = 0;

    for (let i = 0; i < gas.length; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
        gasTank += gas[i] - cost[i];

        if (gasTank < 0) {
            start = i + 1;
            gasTank = 0;
        }
    }

    if (totalGas < totalCost) {
        return -1;
    } else {
        return start;
    }
}
describe('TestCanCompleteCircuit', () => {
  describe('Single Station Tests', () => {
      test('Possible single station', () => {
          const gas = [5];
          const cost = [4];
          const expected = 0;
          expect(canCompleteCircuit(gas, cost)).toBe(expected);
      });

      test('Impossible single station', () => {
          const gas = [4];
          const cost = [5];
          const expected = -1;
          expect(canCompleteCircuit(gas, cost)).toBe(expected);
      });
  });

  describe('Two Stations Tests', () => {
      test('Two stations possible', () => {
          const gas = [1, 2];
          const cost = [2, 1];
          const expected = 1;
          expect(canCompleteCircuit(gas, cost)).toBe(expected);
      });
  });

  describe('Circular Route Tests', () => {
      test('Circular route possible', () => {
          const gas = [1, 2, 3, 4, 5];
          const cost = [3, 4, 5, 1, 2];
          const expected = 3;
          expect(canCompleteCircuit(gas, cost)).toBe(expected);
      });

      test('Circular route impossible', () => {
          const gas = [2, 3, 4];
          const cost = [3, 4, 3];
          const expected = -1;
          expect(canCompleteCircuit(gas, cost)).toBe(expected);
      });
  });
});
