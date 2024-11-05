function handleNestedData(data: any): any {
  if (typeof data === 'object' && data !== null) {
      if (Array.isArray(data)) {
          // If it's an array, apply the function recursively to each item
          return data.map(item => handleNestedData(item));
      } else {
          // If it's an object (dictionary), apply the function recursively to each value
          const result: {[key: string]: any} = {};
          for (const key in data) {
              if (data.hasOwnProperty(key)) {
                  result[key] = handleNestedData(data[key]);
              }
          }
          return result;
      }
  } else if (typeof data === 'string') {
      // Try to convert strings that represent integers or floats to their numeric forms
      const intVal = parseInt(data);
      if (!isNaN(intVal)) {
          return intVal;
      }
      const floatVal = parseFloat(data);
      if (!isNaN(floatVal)) {
          return floatVal;
      }
      return data;  // Return the original string if it's not a number
  } else if (typeof data === 'number') {
      // If it's already a number, return as is
      return data;
  } else if (typeof data === 'bigint' || typeof data === 'boolean' || data === null) {
      // Return the value as is for other primitive types
      return data;
  } else if (Buffer.isBuffer(data)) {
      // If it's a Buffer (equivalent to bytes in Python), decode to a UTF-8 string
      return data.toString('utf8');
  }
  return data;  // Return the input as is for any other type
}