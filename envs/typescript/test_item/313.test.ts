/**
 * @jest-environment jsdom
 */// ... (previous code for context)
import { JSDOM } from 'jsdom';

function isBackgroundTooDarkOrBright(): string {
  const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
  const document = dom.window.document;
  const body = document.body;
  const bgColor = window.getComputedStyle(body).backgroundColor;

  const rgb = bgColor.match(/\d+/g).map(Number);
  const luminance = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2];

  if (luminance > 180) {
    return 'bright';
  } else if (luminance < 60) {
    return 'dark';
  } else {
    return 'normal';
  }
}
// ... (continuation of the code)
describe('isBackgroundTooDarkOrBright', () => {
    let mainElement: HTMLElement;

    beforeEach(() => {
        // Create a 'main' element and append it to the document body
        mainElement = document.createElement('main');
        document.body.appendChild(mainElement);
    });

    afterEach(() => {
        // Clean up by removing the 'main' element after each test
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
