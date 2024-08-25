/**
 * Create and append a specified number of square divs to a container element.
 * @param {number} num - The number of square divs to create.
 * @param {HTMLElement} container - The container to append the divs to.
 */
function createSquareDivs(num, container) {
    // Ensure the container parameter is a valid DOM element
    if (!(container instanceof HTMLElement)) {
        console.error('Invalid container: must be a DOM element.');
        return;
    }

    // Create and append the specified number of square divs
    for (let i = 0; i < num; i++) {
        const square = document.createElement('div');
        square.className = 'square';  // Set the class name for styling purposes
        container.appendChild(square);
    }
}