/**
 * Checks if the provided image question is a valid Base64 encoded image string.
 * 
 * @param {string} imageData - The image question string to be validated.
 * @returns {boolean} - Returns true if the image question is a valid Base64 encoded image, otherwise false.
 */
function isBase64Image(imageData) {
    const base64ImageRegex = /^data:image\/(png|jpe?g|gif|webp);base64,/;
    return base64ImageRegex.test(imageData);
}
