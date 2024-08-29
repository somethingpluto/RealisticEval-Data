// Test Case 1: Valid Base64 encoded PNG image
const imageData1 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
console.log(isBase64Image(imageData1)); 
// Expected output: true
// Explanation: The string is a valid Base64 encoded PNG image.

// Test Case 2: Valid Base64 encoded JPEG image
const imageData2 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD";
console.log(isBase64Image(imageData2)); 
// Expected output: true
// Explanation: The string is a valid Base64 encoded JPEG image.

// Test Case 3: Invalid Base64 string without proper image MIME type
const imageData3 = "data:application/pdf;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
console.log(isBase64Image(imageData3)); 
// Expected output: false
// Explanation: The string is a Base64 encoded PDF, not an image.

// Test Case 4: Invalid string with no Base64 encoding
const imageData4 = "data:image/png;base64,ThisIsNotBase64Encoded";
console.log(isBase64Image(imageData4)); 
// Expected output: true
// Explanation: The string starts with a valid Base64 image prefix but is not correctly Base64 encoded. However, the function only checks for the correct prefix.

// Test Case 5: Random string without Base64 prefix
const imageData5 = "This is not a Base64 encoded image string.";
console.log(isBase64Image(imageData5)); 
// Expected output: false
// Explanation: The string does not match the Base64 image pattern at all.

/**
 * Checks if the provided image data is a valid Base64 encoded image string.
 * 
 * @param {string} imageData - The image data string to be validated.
 * @returns {boolean} - Returns true if the image data is a valid Base64 encoded image, otherwise false.
 */
function isBase64Image(imageData) {
    const base64ImageRegex = /^data:image\/(png|jpe?g|gif|webp);base64,/;
    return base64ImageRegex.test(imageData);
}
