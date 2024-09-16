/**
 * Detecting the light or dark state of the background element of a major element of a web page and returning the corresponding description string
 *
 * @returns {string} - Returns "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
 */
function isBackgroundTooDarkOrBright() {
    // Get the computed style of the main element
    const mainElement = document.querySelector('main');
    const computedStyle = getComputedStyle(mainElement);

    // Extract the background color as a string
    const backgroundColor = computedStyle.backgroundColor;

    // Convert the background color to RGB components
    const rgb = backgroundColor.match(/\d+/g).map(Number);
    const [r, g, b] = rgb;

    // Calculate the perceived brightness using the formula
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;

    // Define thresholds for darkness and brightness
    const darkThreshold = 125;
    const brightThreshold = 200;

    // Determine and return the background brightness level
    if (brightness < darkThreshold) {
        return "dark";
    } else if (brightness > brightThreshold) {
        return "bright";
    } else {
        return "normal";
    }
}
