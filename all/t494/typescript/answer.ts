import { isNaN } from 'lodash';

function cleanObject(inputObj: Record<string, any>): Record<string, any> {
  const cleanedObj: Record<string, any> = {};

  for (const [key, value] of Object.entries(inputObj)) {
    // Check if the value is not null and not a whitespace string
    if (value !== null && (typeof value === 'string' && value.trim() !== '')) {
      // Check if value is a number (int or float) and is not NaN
      if (!(typeof value === 'number' && isNaN(value))) {
        cleanedObj[key] = value;
      }
    }
  }

  return cleanedObj;
}