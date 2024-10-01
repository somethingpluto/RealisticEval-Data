describe('isTouchDevice', () => {
    beforeEach(() => {
        // Reset window and navigator before each test
        Object.defineProperty(window, 'ontouchstart', { value: undefined, writable: true });
        Object.defineProperty(navigator, 'maxTouchPoints', { value: undefined, writable: true });
        Object.defineProperty(navigator, 'msMaxTouchPoints', { value: undefined, writable: true });
    });

    test('should return true for a device with touch events supported', () => {
        Object.defineProperty(window, 'ontouchstart', { value: true, writable: true });
        expect(isTouchDevice()).toBe(true);
    });

    test('should return true if maxTouchPoints is greater than 0', () => {
        Object.defineProperty(navigator, 'maxTouchPoints', { value: 2, writable: true });
        expect(isTouchDevice()).toBe(true);
    });

    test('should return true if msMaxTouchPoints is greater than 0', () => {
        Object.defineProperty(navigator, 'msMaxTouchPoints', { value: 3, writable: true });
        expect(isTouchDevice()).toBe(true);
    });

    test('should return false if touch events are not supported and maxTouchPoints is 0', () => {
        Object.defineProperty(window, 'ontouchstart', { value: false, writable: true });
        Object.defineProperty(navigator, 'maxTouchPoints', { value: 0, writable: true });
        Object.defineProperty(navigator, 'msMaxTouchPoints', { value: 0, writable: true });
        expect(isTouchDevice()).toBe(false);
    });

    test('should return false if navigator properties are undefined', () => {
        // Keeping them undefined as defined in the beforeEach
        expect(isTouchDevice()).toBe(false);
    });

    test('should return true if any of the properties indicate a touch device', () => {
        // Test mixed cases where ontouchstart is undefined and maxTouchPoints is > 0
        Object.defineProperty(window, 'ontouchstart', { value: undefined, writable: true });
        Object.defineProperty(navigator, 'maxTouchPoints', { value: 1, writable: true });
        expect(isTouchDevice()).toBe(true);
    });
});