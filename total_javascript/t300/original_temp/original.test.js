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
// u/name     Instacart Ad Remover
// u/description Removes all sponsored products from Instacart, so you can make quicker and better buying decisions :) created using GPT-4
// u/version  1
// u/grant    none
// u/match    *://*.instacart.com/*
// ==/UserScript==
function removeAds() {
    const allLiElements = document.getElementsByTagName('li');

    for (let i = 0; i < allLiElements.length; i++) {
        const li = allLiElements[i];

        // Find the 'sponsored' indicators
        const sponsoredIndicators = li.getElementsByClassName('css-16lshh0');

        // If this 'li' element contains a 'sponsored' indicator, remove the 'li' element
        if (sponsoredIndicators.length > 0) {
            li.parentNode.removeChild(li);
        }
    }
}

// Run the 'removeAds' function every second
setInterval(removeAds, 1000);