function uint8ArrayToBase64(uint8Array: Uint8Array): string {
    let base64 = "";
    const characters =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  
    for (let i = 0; i < uint8Array.length; i += 3) {
      const a = uint8Array[i];
      const b = uint8Array[i + 1];
      const c = uint8Array[i + 2];
  
      const index1 = a >> 2;
      const index2 = ((a & 0x03) << 4) | (b >> 4);
      const index3 = ((b & 0x0f) << 2) | (c >> 6);
      const index4 = c & 0x3f;
  
      base64 +=
        characters[index1] +
        characters[index2] +
        characters[index3] +
        characters[index4];
    }
  
    return base64;
  }