
function testBase64ToArrayBuffer() {
  const testCases = [
      { base64: "SGVsbG8sIFdvcmxkIQ==", expected: "Hello, World!" },
      { base64: "U29tZSB0ZXh0IHdpdGggc3BhcmluZyBhbmQgd29ya2luZyE=", expected: "Some text with sparing and working!" },
      { base64: "QmFzZTY0IGVuY29kaW5nIGlzIGEgY29tbW9ubG9nIEZvciBiaW5hcnkgZGF0YQ==", expected: "Base64 encoding is a common log For binary data" },
      { base64: "R2l2ZSBtZSBhbG9uZyBhIHBhdGggdG8gY29tcGxldGUgc3RhcnQgcGFnZS4=", expected: "Give me along a path to complete start page." },
      { base64: "SW4gYmFzZTY0IGVuY29kaW5nLCB0aGlzIGlzIGFuIGV4YW1wbGUgYXJlYS=", expected: "In base64 encoding, this is an example area." }
  ];

  testCases.forEach(({ base64, expected }, index) => {
      const arrayBuffer = base64ToArrayBuffer(base64);
      const decoder = new TextDecoder();
      const result = decoder.decode(arrayBuffer);

      console.log(`Test Case ${index + 1}`);
      console.log(`Base64 String: ${base64}`);
      console.log(`Decoded Result: ${result}`);
      console.log(`Expected Result: ${expected}`);
      console.log(`Test Passed: ${result === expected}`);
      console.log('---');
  });
}

testBase64ToArrayBuffer();



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