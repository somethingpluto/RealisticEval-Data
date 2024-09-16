function arrayBufferToString(buffer: ArrayBuffer): string {
    const uint8Array = new Uint8Array(buffer);
    const array = Array.from(uint8Array);
    return String.fromCharCode.apply(null, array);
  }