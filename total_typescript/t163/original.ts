function binaryStringToUint8Array(binaryStr: string): Uint8Array {
    const byteCount = Math.ceil(binaryStr.length / 8);
    const byteArray = new Uint8Array(byteCount);
  
    for (let i = 0; i < byteCount; i++) {
      byteArray[i] = parseInt(binaryStr.substr(i * 8, 8), 2);
    }
  
    return byteArray;
  }