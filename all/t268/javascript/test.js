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