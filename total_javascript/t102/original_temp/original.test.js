// Test Case 1: Element with a known font size.
document.body.innerHTML = '<div id="test1" style="font-size: 16px;"></div>';
console.log(getFontSizeFromID('test1')); // Expected output: 16

// Test Case 2: Element with a different font size.
document.body.innerHTML = '<div id="test2" style="font-size: 24px;"></div>';
console.log(getFontSizeFromID('test2')); // Expected output: 24

// Test Case 3: Element with inherited font size (no explicit font-size set).
document.body.innerHTML = '<div id="test3" style="font-size: 20px;"><span id="child"></span></div>';
console.log(getFontSizeFromID('child')); // Expected output: 20

// Test Case 4: Element with a non-pixel font size (e.g., em, rem).
document.body.innerHTML = '<div id="test4" style="font-size: 1.5em;"></div>';
console.log(getFontSizeFromID('test4')); // Expected output: Depends on the parent font size (e.g., 24 if parent is 16px)

// Test Case 5: Element does not exist.
console.log(getFontSizeFromID('nonExistentID')); // Expected output: NaN (or error handling, depending on implementation)

function getFontSizeFromID(id) {
    const el = document.getElementById(id);
    const fontSize = parseInt(window.getComputedStyle(el).fontSize);
    return fontSize;
}

function getScrollbarWidth() {
    // This function was generated by ChatGPT-3
    // Create a dummy element with a scrollbar
    const scrollDiv = document.createElement('div');
    scrollDiv.style.width = '100px';
    scrollDiv.style.height = '100px';
    scrollDiv.style.overflow = 'scroll';

    // Append the dummy element to the document
    document.body.appendChild(scrollDiv);

    // Calculate the scrollbar width
    const scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;

    // Remove the dummy element from the document
    document.body.removeChild(scrollDiv);

    return scrollbarWidth;
}

export { getFontSizeFromID, getScrollbarWidth };