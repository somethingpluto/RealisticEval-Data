/**
 * Converts an image to a binary representation. Convert the image to black and white mode,
 * that is, each pixel is represented by only 1 bit, with a white pixel value of 255 and a black pixel value of 0.
 *
 * @param {string} imagePath - The file path of the image to convert.
 * @returns {Array<number>} - A list of bits representing the image, where 1 is for white pixels
 *                          and 0 is for black pixels.
 */
async function convertImageToBits(imagePath) {
    // Load the image using the HTML Image element
    const img = new Image();
    return new Promise((resolve, reject) => {
        img.onload = () => {
            // Create a canvas element to draw the image on
            const canvas = document.createElement('canvas');
            canvas.width = img.width;
            canvas.height = img.height;

            // Get the drawing context of the canvas
            const ctx = canvas.getContext('2d');

            // Draw the image onto the canvas
            ctx.drawImage(img, 0, 0);

            // Get the image data from the canvas
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imageData.data;

            // Initialize an array to store the bits
            const bits = [];

            // Iterate over each pixel in the image data
            for (let i = 0; i < data.length; i += 4) {
                // Extract the red component (since it's a grayscale image)
                const r = data[i];

                // Determine if the pixel is white or black
                const bit = r === 255 ? 1 : 0;

                // Add the bit to the bits array
                bits.push(bit);
            }

            // Resolve the promise with the bits array
            resolve(bits);
        };

        img.onerror = (error) => {
            // Reject the promise if there was an error loading the image
            reject(error);
        };

        // Set the source of the image to the provided image path
        img.src = imagePath;
    });
}