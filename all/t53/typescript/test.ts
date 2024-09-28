import { sizeInBytes } from './yourModule'; // Import your sizeInBytes function from its module

describe('sizeInBytes', () => {

  test('size of integer', () => {
    const integerValue = 42;
    // Expect some reasonable estimation since we can't directly replicate sys.getsizeof
    const resultSize = sizeInBytes(integerValue);
    // This is a placeholder as we can't get the exact size directly like Python
    const expectedSize = 0; // Adjust based on what your function returns
    expect(resultSize).toBe(expectedSize);
  });

  test('size of string', () => {
    const stringValue = "Hello, world!";
    const resultSize = sizeInBytes(stringValue);
    const expectedSize = Buffer.byteLength(stringValue, 'utf8');
    expect(resultSize).toBe(expectedSize);
  });

  test('size of list', () => {
    const listValue = [1, 2, 3, 4, 5];
    const resultSize = sizeInBytes(listValue);
    // You will need to calculate the expected size based on your approximation logic
    const expectedSize = listValue.reduce((sum, item) => sum + sizeInBytes(item), 0);
    expect(resultSize).toBe(expectedSize);
  });

  test('size of dictionary', () => {
    const dictValue = { 'key1': 'value1', 'key2': 'value2' };
    const resultSize = sizeInBytes(dictValue);
    // Again calculate based on your approximation method
    const expectedSize = 'key1'.length + sizeInBytes(dictValue['key1']) +
                         'key2'.length + sizeInBytes(dictValue['key2']);
    expect(resultSize).toBe(expectedSize);
  });

  test('size of custom object', () => {
    class CustomObject {
      attr1 = 'a';
      attr2 = 123;
    }
    const customObj = new CustomObject();
    const resultSize = sizeInBytes(customObj);
    // Calculate expected size based on your approximation method
    const expectedSize = sizeInBytes('attr1') + sizeInBytes(customObj.attr1) +
                         sizeInBytes('attr2') + sizeInBytes(customObj.attr2);
    expect(resultSize).toBe(expectedSize);
  });

});