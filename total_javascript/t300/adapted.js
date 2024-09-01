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