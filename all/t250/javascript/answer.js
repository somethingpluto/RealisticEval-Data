function invertDictionary(originalDict) {
  let invertedDict = {};

  for (let key in originalDict) {
    if (!invertedDict[originalDict[key]]) {
      invertedDict[originalDict[key]] = [key];
    } else {
      invertedDict[originalDict[key]].push(key);
    }
  }

  return invertedDict;
}