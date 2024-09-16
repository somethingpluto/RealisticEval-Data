function base64ToArrayBuffer(base64: string): ArrayBuffer {
    const binaryString = atob(base64);
    const length = binaryString.length;
    const buffer = new ArrayBuffer(length);
    const bufferView = new Uint8Array(buffer);
    for (let i = 0; i < length; i++) {
      bufferView[i] = binaryString.charCodeAt(i);
    }
    return buffer;
  }