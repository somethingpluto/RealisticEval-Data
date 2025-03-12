import { Fraction } from 'fraction.js';

function convertScoreToDecimal(scoreStr: string): number | null {
    const parts = scoreStr.split('/');
    if (parts.length !== 2 || isNaN(Number(parts[0])) || isNaN(Number(parts[1]))) {
        return null;
    }
    const numerator = new Fraction(parts[0]);
    const denominator = new Fraction(parts[1]);
    return numerator.div(denominator).valueOf();
}
describe('TestConvertScoreToDecimal', () => {
  it('should correctly convert a simple decimal score', () => {
    expect(convertScoreToDecimal("2.5")).toEqual(2.5);
  });

  it('should correctly convert a fraction score', () => {
    expect(convertScoreToDecimal("10/4")).toEqual(2.5);
  });

  it('should correctly convert an integer score represented as a string', () => {
    expect(convertScoreToDecimal("5")).toEqual(5.0);
  });

  it('should correctly convert an integer division score', () => {
    expect(convertScoreToDecimal("12/3")).toEqual(4.0);
  });
});
