function safeSplice(inputArray, amountToRemove,indexToRemove,replaceWith) {
    let array1 = inputArray.slice(0, indexToRemove )
  if (replaceWith!=undefined){
  array1.push(replaceWith)}
    let array2 = inputArray.slice(indexToRemove + amountToRemove, inputArray.length)
    return array1.concat(array2)
  }
  