/**
         * Create a mosaic of a given p5.js sketch.
         * Created using ChatGPT-3.5-turbo:
         * https://chat.openai.com/share/a88e18c4-7a2f-467f-9933-53df1d5faf3e
         */
// Function to create iframes and load the sketch from a file
function createIframe(url, size) {
    let iframe = document.createElement('iframe');
    iframe.src = url;
    iframe.width = size;
    iframe.height = size;
    iframe.onload = function () {
        iframe.classList.add('fade-in'); // Add the fade-in class after iframe has loaded
    };
    document.body.appendChild(iframe);
}
