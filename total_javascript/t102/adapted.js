/**
 * Retrieves the font size of the element with the specified ID.
 * 
 * @param {string} id - The ID of the element.
 * @returns {number} - The font size of the element in pixels.
 */
function getFontSizeFromID(id) {
    const element = document.getElementById(id);
    const fontSize = parseInt(window.getComputedStyle(element).fontSize);
    return fontSize;
}

/**
 * Calculates the width of the browser's scrollbar.
 * 
 * @returns {number} - The width of the scrollbar in pixels.
 */
function getScrollbarWidth() {
    // Create a temporary element with a scrollbar
    const scrollDiv = document.createElement('div');
    scrollDiv.style.width = '100px';
    scrollDiv.style.height = '100px';
    scrollDiv.style.overflow = 'scroll';

    // Append the temporary element to the document body
    document.body.appendChild(scrollDiv);

    // Calculate the scrollbar width
    const scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;

    // Remove the temporary element from the document body
    document.body.removeChild(scrollDiv);

    return scrollbarWidth;
}

export { getFontSizeFromID, getScrollbarWidth };
