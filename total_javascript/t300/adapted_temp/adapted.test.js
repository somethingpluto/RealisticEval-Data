/**
 * @jest-environment jsdom
 */

describe('removeAds', () => {
    beforeEach(() => {
        // Reset the DOM before each test
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
        expect(listItems.length).toBe(1);
        expect(listItems[0].textContent).toBe('Regular Item');
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
        expect(listItems.length).toBe(2);
        expect(listItems[0].textContent).toBe('Regular Item');
        expect(listItems[1].textContent).toBe('Another Regular Item');
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
        expect(listItems.length).toBe(1);
        expect(listItems[0].textContent).toBe('Regular Item');
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

// ==UserScript==
// @name         Instacart Ad Remover
// @description  Iterate over list items on a web page and remove ads that contain a specific class name
// @version      1.1
// @grant        none
// @match        *://*.instacart.com/*
// ==/UserScript==
function removeAds() {
    // Get all 'li' elements on the page
    const listItems = document.querySelectorAll('li');

    listItems.forEach((item) => {
        // Check for the presence of a sponsored indicator
        const isSponsored = item.querySelector('.css-16lshh0');

        // If a sponsored indicator is found, remove the 'li' element
        if (isSponsored) {
            item.remove();
        }
    });
}

// Run the 'removeSponsoredAds' function every second
setInterval(removeAds, 1000);