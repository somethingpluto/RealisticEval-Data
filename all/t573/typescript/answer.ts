function isTouchDevice(): boolean {
    // Check if the 'ontouchstart' event is supported
    const hasTouchEvent = 'ontouchstart' in window;

    // Check the maximum number of touch points supported
    const maxTouchPoints = navigator.maxTouchPoints !== undefined ? navigator.maxTouchPoints > 0 : false;

    // For Internet Explorer and older browsers
    const msMaxTouchPoints = navigator.msMaxTouchPoints !== undefined ? navigator.msMaxTouchPoints > 0 : false;

    // Return true if any of the checks indicate a touch device
    return hasTouchEvent || maxTouchPoints || msMaxTouchPoints;
}