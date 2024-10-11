function flattenArray(multiDimArray) {
  let result = [];

  function flatten(subArray) {
    for(let i=0; i<subArray.length; i++) {
      if(Array.isArray(subArray[i])) {
        flatten(subArray[i]);
      } else {
        result.push(subArray[i]);
      }
    }
  }

  flatten(multiDimArray);

  return result;
}