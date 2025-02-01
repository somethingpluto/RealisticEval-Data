/**
 * @jest-environment jsdom
 *//**
 * Iterate over list items on a web page and remove ads that contain a specific class name
 */
function removeAds() {
    // Get all list items on the page
    const listItems = document.querySelectorAll('li');

    // Iterate over each list item
    listItems.forEach(item => {
        // Check if the list item contains the ad class
        if (item.classList.contains('ad-class')) {
            // Remove the ad list item from the DOM
            item.remove();
        }
    });
}
describe('removeAds', () => {
    beforeEach(() => {
        // Reset the DOM before each test.js
        document.body.innerHTML = '';
    });

    test('removes a single sponsored product', () => {
        document.body.innerHTML = `
            <ul>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Regular Item</li>
            </ul>
        `;

        removeAds();

        const listItems = document.querySelectorAll('li');
        expect(listItems.length).toBe(2);
        expect(listItems[0].textContent).toBe('Sponsored');
    });

    test('removes multiple sponsored products', () => {
        document.body.innerHTML = `
            <ul>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Regular Item</li>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Another Regular Item</li>
            </ul>
        `;

        removeAds();

        const listItems = document.querySelectorAll('li');
        expect(listItems.length).toBe(4);
        expect(listItems[0].textContent).toBe('Sponsored');
        expect(listItems[1].textContent).toBe('Regular Item');
    });

    test('does not remove any items if there are no sponsored products', () => {
        document.body.innerHTML = `
            <ul>
                <li>Regular Item</li>
                <li>Another Regular Item</li>
            </ul>
        `;

        removeAds();

        const listItems = document.querySelectorAll('li');
        expect(listItems.length).toBe(2);
        expect(listItems[0].textContent).toBe('Regular Item');
        expect(listItems[1].textContent).toBe('Another Regular Item');
    });

    test('removes items with nested sponsored indicators', () => {
        document.body.innerHTML = `
            <ul>
                <li>
                    <div>
                        <span class="css-16lshh0">Sponsored</span>
                    </div>
                </li>
                <li>Regular Item</li>
            </ul>
        `;

        removeAds();

        const listItems = document.querySelectorAll('li');
        expect(listItems.length).toBe(2);
    });

    test('does not remove items with similar but non-sponsored class names', () => {
        document.body.innerHTML = `
            <ul>
                <li><span class="css-16lshh1">Not Sponsored</span></li>
                <li>Regular Item</li>
            </ul>
        `;

        removeAds();

        const listItems = document.querySelectorAll('li');
        expect(listItems.length).toBe(2);
        expect(listItems[0].textContent).toBe('Not Sponsored');
        expect(listItems[1].textContent).toBe('Regular Item');
    });
});


