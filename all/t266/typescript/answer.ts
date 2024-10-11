import { isObject, isArray } from 'lodash';

interface QuestionObject {
  [key: string]: any;
}

function handleNestedData(data: QuestionObject): QuestionObject {
  /**
   * Handle nested question structures (e.g., objects, arrays, and enums), decode bytes to UTF-8 strings,
   * and convert numbers to integers or floating point numbers.
   *
   * @param data - The question object to be processed.
   * @returns The converted question object.
   */

  const processValue = (value: any): any => {
    if (typeof value === 'string' && value.startsWith('b\'')) {
      // Assuming the byte string starts with 'b\'' and ends with '\''
      try {
        return Buffer.from(value.slice(2, -1), 'hex').toString('utf-8');
      } catch (error) {
        console.error('Failed to decode byte string:', error);
        return value; // Return original value on failure
      }
    }

    if (typeof value === 'number') {
      return Number.isInteger(value) ? Math.floor(value) : parseFloat(value.toFixed(2));
    }

    if (isObject(value)) {
      return Object.keys(value).reduce((acc, key) => {
        acc[key] = processValue(value[key]);
        return acc;
      }, {} as QuestionObject);
    }

    if (isArray(value)) {
      return value.map(processValue);
    }

    return value;
  };

  return processValue(data);
}