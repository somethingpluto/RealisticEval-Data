// Import the createSquareDivs function if it's in another file
// const createSquareDivs = require('./path_to_your_file');

describe('createSquareDivs', () => {
    let container;

    // Setup a DOM-like environment for each test
    beforeEach(() => {
        document.body.innerHTML = '<div id="test-container"></div>';
        container = document.getElementById('test-container');
    });

    test('correctly creates and appends the specified number of divs', () => {
        createSquareDivs(3, container);
        expect(container.children.length).toBe(3);
        expect(container.children[0].className).toBe('square');
    });

    test('appends zero divs when the specified number is zero', () => {
        createSquareDivs(0, container);
        expect(container.children.length).toBe(0);
    });

    test('handles negative numbers by not creating any divs', () => {
        createSquareDivs(-5, container);
        expect(container.children.length).toBe(0);
    });

    test('ensures all created divs have the correct class', () => {
        createSquareDivs(5, container);
        const allHaveClassSquare = Array.from(container.children).every(child => child.className === 'square');
        expect(allHaveClassSquare).toBe(true);
    });

    test('throws an error if container is not a valid DOM element', () => {
        const fakeContainer = {}; // Not a DOM element
        expect(() => createSquareDivs(1, fakeContainer)).toThrow('Invalid container: must be a DOM element.');
    });
});