/**
 * Handles nested data structures (e.g., objects, arrays) by decoding bytes to UTF-8 strings and converting numbers to integers or floating-point numbers.
 * @param {Object} data - The data object to be processed.
 * @returns {Object} - The processed data.
 */
function handleNestedData(data) {
  // Helper function to process individual values
  function processValue(value) {
    if (typeof value === 'string') {
      // Attempt to decode bytes to UTF-8 string
      try {
        return decodeURIComponent(escape(value));
      } catch (e) {
        // If decoding fails, return the original string
        return value;
      }
    } else if (typeof value === 'number') {
      // Convert numbers to integers or floating-point numbers
      if (Number.isInteger(value)) {
        return parseInt(value, 10);
      } else {
        return parseFloat(value);
      }
    } else {
      // Return the value as is for non-string and non-number types
      return value;
    }
  }

  // Recursively process the data object
  function processObject(obj) {
    const processedObj = {};
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        const value = obj[key];
        if (typeof value === 'object' && value !== null) {
          // Recursively process nested objects or arrays
          processedObj[key] = Array.isArray(value) ? processArray(value) : processObject(value);
        } else {
          // Process individual values
          processedObj[key] = processValue(value);
        }
      }
    }
    return processedObj;
  }

  // Recursively process the data array
  function processArray(arr) {
    return arr.map(item => {
      if (typeof item === 'object' && item !== null) {
        // Recursively process nested objects or arrays
        return Array.isArray(item) ? processArray(item) : processObject(item);
      } else {
        // Process individual values
        return processValue(item);
      }
    });
  }

  // Start processing from the root of the data
  if (Array.isArray(data)) {
    return processArray(data);
  } else {
    return processObject(data);
  }
}
describe('TestHandleNestedData', () => {
  describe('test_simple_dictionary', () => {
      it('should correctly handle a simple dictionary', () => {
          const data = { name: Buffer.from('Alice'), age: '30' };
          const expected = { name: 'Alice', age: 30 };
          expect(handleNestedData(data)).toEqual(expected);
      });
  });

  describe('test_nested_dictionary', () => {
      it('should correctly handle a nested dictionary', () => {
          const data = { user: { name: Buffer.from('Bob'), details: { age: '25', height: '175.5' } } };
          const expected = { user: { name: 'Bob', details: { age: 25, height: 175.5 } } };
          expect(handleNestedData(data)).toEqual(expected);
      });
  });

  describe('test_list_of_mixed_data_types', () => {
      it('should correctly handle a list of mixed data types', () => {
          const data = ['100', Buffer.from('200'), 300.0, '400.5'];
          const expected = [100, '200', 300.0, 400.5];
          expect(handleNestedData(data)).toEqual(expected);
      });
  });

  describe('test_incorrect_byte_decoding', () => {
      it('should throw an error when decoding invalid bytes', () => {
          const data = { invalid_bytes: Buffer.from('\xff\xfe\xfd\xfc') };
          expect(() => handleNestedData(data)).toThrow(/UnicodeDecodeError/);
      });
  });

  describe('test_complex_nested_structure', () => {
      it('should correctly handle a complex nested structure', () => {
          const data = {
              team: [
                  { name: Buffer.from('Charlie'), scores: ['1000', '2000.2'] },
                  { name: Buffer.from('Daisy'), skills: [Buffer.from('Coding'), 'Design'], age: '22' }
              ]
          };
          const expected = {
              team: [
                  { name: 'Charlie', scores: [1000, 2000.2] },
                  { name: 'Daisy', skills: ['Coding', 'Design'], age: 22 }
              ]
          };
          expect(handleNestedData(data)).toEqual(expected);
      });
  });
});
