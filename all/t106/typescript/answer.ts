function isBase64Image(imageData: string): boolean {
    // Check if the input is a non-empty string
    if (typeof imageData !== 'string' || imageData.trim() === '') {
        return false;
    }

    // Regular expression to validate a Base64 image string
    const base64ImagePattern = /^data:image\/(jpeg|png|gif|bmp|webp);base64,[A-Za-z0-9+/]+={0,2}$/;

    // Test the image data against the pattern
    return base64ImagePattern.test(imageData);
}