function numericalStrConvert(value) {
  // check if value is an integer
  const intValue = parseInt(value);
  if (!isNaN(intValue)) {
    return intValue;
  }

  // check if value is a floating point number
  const floatValue = parseFloat(value);
  if (!isNaN(floatValue)) {
    return floatValue;
  }

  // if neither, return the original string
  return value;
}