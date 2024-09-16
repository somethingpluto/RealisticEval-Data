/**
 * Create a mosaic of a given p5.js sketch.
 * Created using ChatGPT-3.5-turbo:
 * https://chat.openai.com/share/a88e18c4-7a2f-467f-9933-53df1d5faf3e
 */
function createIframe(url, size) {
    const iframe = document.createElement('iframe');
    iframe.src = url;
    iframe.style.width = `${size}px`;
    iframe.style.height = `${size}px`;

    iframe.addEventListener('load', () => {
        iframe.classList.add('fade-in');
    });

    document.body.appendChild(iframe);
}
