/**
 * @jest-environment jsdom
 */

describe('isBackgroundTooDarkOrBright', () => {
    let mainElement;

    beforeEach(() => {
        // Create a 'main' element and append it to the document body
        mainElement = document.createElement('main');
        document.body.appendChild(mainElement);
    });

    afterEach(() => {
        // Clean up by removing the 'main' element after each test.js
        document.body.removeChild(mainElement);
    });

    test('should return "dark" for a dark background color', () => {
        // Set a dark background color
        mainElement.style.backgroundColor = 'rgb(30, 30, 30)';

        const result = isBackgroundTooDarkOrBright();
        expect(result).toBe('dark');
    });

    test('should return "bright" for a bright background color', () => {
        // Set a bright background color
        mainElement.style.backgroundColor = 'rgb(250, 250, 250)';

        const result = isBackgroundTooDarkOrBright();
        expect(result).toBe('bright');
    });

    test('should return "normal" for a background color with normal brightness', () => {
        // Set a background color with normal brightness
        mainElement.style.backgroundColor = 'rgb(150, 150, 150)';

        const result = isBackgroundTooDarkOrBright();
        expect(result).toBe('normal');
    });

    test('should correctly handle a bright color with high red component', () => {
        // Set a bright color with a high red component
        mainElement.style.backgroundColor = 'rgb(255, 100, 100)';

        const result = isBackgroundTooDarkOrBright();
        expect(result).toBe('normal');
    });

    test('should correctly handle a dark color with low green and blue components', () => {
        // Set a dark color with low green and blue components
        mainElement.style.backgroundColor = 'rgb(10, 10, 100)';

        const result = isBackgroundTooDarkOrBright();
        expect(result).toBe('dark');
    });
});

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
