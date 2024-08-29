
function arrayBufferToString(buffer: ArrayBuffer): string {
    const uint8Array = new Uint8Array(buffer);
    const array = Array.from(uint8Array);
    return String.fromCharCode.apply(null, array);
}
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
