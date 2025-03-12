import { execSync } from 'child_process';

function cleanPattern(x: string | any, pattern: string): number | '' {
  const inputString = String(x);
  const match = inputString.match(new RegExp(pattern));
  if (match) {
    const extractedValue = parseFloat(match[0]);
    if (!isNaN(extractedValue)) {
      return extractedValue;
    }
  }
  return '';
}

function callPythonScript(input: string): string {
  try {
    const result = execSync(`python process_data.py "${input}"`);
    return result.toString();
  } catch (error) {
    console.error('Error calling Python script:', error);
    return '';
  }
}
describe('TestCleanPattern', () => {
  let pattern: string;

  beforeEach(() => {
    // Sets up a common regex pattern for testing
    pattern = '(\\d+\\.?\\d*) kg';  // Regex pattern to match weight in kg
  });

  it('should handle valid integer weight', () => {
    const inputString = "The weight is 25 kg";
    const result = cleanPattern(inputString, pattern);
    expect(result).toEqual(25.0);
  });

  it('should handle valid float weight', () => {
    const inputString = "Weight measured at 15.75 kg";
    const result = cleanPattern(inputString, pattern);
    expect(result).toEqual(15.75);
  });

  it('should return an empty string when no weight is found', () => {
    const inputString = "No weight provided.";
    const result = cleanPattern(inputString, pattern);
    expect(result).toEqual('');
  });

  it('should return an empty string for non-numeric weight', () => {
    const inputString = "The weight is thirty kg";
    const result = cleanPattern(inputString, pattern);
    expect(result).toEqual('');
  });

  it('should handle weight with extra text', () => {
    const inputString = "The total weight is 45.3 kg as per the last measurement.";
    const result = cleanPattern(inputString, pattern);
    expect(result).toEqual(45.3);
  });
});
