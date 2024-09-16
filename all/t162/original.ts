function boolArrayToBinaryString(boolArray: boolean[]): string {
    let binaryStr = "";
    boolArray.forEach((bool, index) => {
      binaryStr += bool ? "1" : "0";
    });
    return binaryStr;
  }
  