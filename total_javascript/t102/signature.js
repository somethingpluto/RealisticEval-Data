/**
 * Retrieves the font size of the element with the specified ID.
 * 
 * @param {string} id - The ID of the element.
 */
function getFontSizeFromID(id) {
    const element = document.getElementById(id);
    const fontSize = parseInt(window.getComputedStyle(element).fontSize);
    return fontSize;
}

/**
 * Calculates the width of the browser's scrollbar.
 */
function getScrollbarWidth() {
    
}