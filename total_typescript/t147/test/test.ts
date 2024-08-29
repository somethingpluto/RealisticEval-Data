
const buffer1 = new ArrayBuffer(0);
console.log(arrayBufferToString(buffer1)); // Expected: ""
const buffer2 = new TextEncoder().encode("A").buffer;
console.log(arrayBufferToString(buffer2)); // Expected: "A"
const buffer3 = new TextEncoder().encode("Hello").buffer;
console.log(arrayBufferToString(buffer3)); // Expected: "Hello"
const buffer4 = new TextEncoder().encode("¡Hola!").buffer;
console.log(arrayBufferToString(buffer4)); // Expected: "¡Hola!"
const buffer5 = new TextEncoder().encode("Hello 🌍").buffer;
console.log(arrayBufferToString(buffer5)); // Expected: "Hello 🌍"
