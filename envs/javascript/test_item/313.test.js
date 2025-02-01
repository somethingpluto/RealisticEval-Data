/**
 * @jest-environment jsdom
 *//**
 * Detecting the light or dark state of the background element of a major element of a web page and returning the corresponding description string
 *
 * @returns {string} - Returns "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
 */
function isBackgroundTooDarkOrBright() {
  // Select a major element of the web page, for example, the body
  const element = document.body;

  // Get the computed style of the element
  const style = window.getComputedStyle(element);

  // Extract the background color
  const bgColor = style.backgroundColor;

  // Parse the background color to RGB
  const rgb = parseColor(bgColor);

  // Calculate the luminance of the background color
  const luminance = calculateLuminance(rgb);

  // Define thresholds for dark and bright
  const darkThreshold = 50; // Adjust this value as needed
  const brightThreshold = 200; // Adjust this value as needed

  // Determine if the background is too dark, too bright, or normal
  if (luminance < darkThreshold) {
    return "dark";
  } else if (luminance > brightThreshold) {
    return "bright";
  } else {
    return "normal";
  }
}

// Helper function to parse a CSS color value to RGB
function parseColor(color) {
  if (color.startsWith("rgb")) {
    // Remove the 'rgb(' and ')' from the string
    color = color.substring(4, color.length - 1);
    // Split the string into an array of numbers
    const values = color.split(",");
    // Convert the array of strings to an array of numbers
    return values.map(value => parseInt(value.trim()));
  } else {
    // If the color is not in RGB format, return null
    return null;
  }
}

// Helper function to calculate the luminance of an RGB color
function calculateLuminance(rgb) {
  // Calculate the luminance using the formula for sRGB
  const r = rgb[0] / 255;
  const g = rgb[1] / 255;
  const b = rgb[2] / 255;
  return 0.2126 * (r <= 0.03928 ? r / 12.92 : Math.pow((r + 0.055) / 1.055, 2.4)) +
         0.7152 * (g <= 0.03928 ? g / 12.92 : Math.pow((g + 0.055) / 1.055, 2.4)) +
         0.0722 * (b <= 0.03928 ? b / 12.92 : Math.pow((b + 0.055) / 1.055, 2.4));
}
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

