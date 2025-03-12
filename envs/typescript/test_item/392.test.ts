// ... (previous code for context)

function lookAndSay(number: string): string {
    let nextSequence = '';
    let count = 1;

    for (let i = 0; i < number.length; i++) {
        if (number[i] === number[i + 1]) {
            count++;
        } else {
            nextSequence += count.toString() + number[i];
            count = 1;
        }
    }

    return nextSequence;
}

// Unit tests
function testLookAndSay() {
    console.assert(lookAndSay('1') === '11', 'Test failed for input "1".');
    console.assert(lookAndSay('11') === '21', 'Test failed for input "11".');
    console.assert(lookAndSay('21') === '1211', 'Test failed for input "21".');
    console.assert(lookAndSay('1211') === '111221', 'Test failed for input "1211".');
    console.assert(lookAndSay('111221') === '312211', 'Test failed for input "111221".');
    console.log('All tests passed!');
}

testLookAndSay();

// ... (rest of the code)
describe('TestLookAndSay', () => {
    it('should replicate a single digit correctly', () => {
      expect(lookAndSay('1')).toBe('11');
    });
  
    it('should handle a sequence of the same digits', () => {
      expect(lookAndSay('111')).toBe('31');
    });
  
    it('should handle a sequence with different digits', () => {
      expect(lookAndSay('1211')).toBe('111221');
    });
  
    it('should handle a more complex sequence', () => {
      expect(lookAndSay('312211')).toBe('13112221');
    });
  });
