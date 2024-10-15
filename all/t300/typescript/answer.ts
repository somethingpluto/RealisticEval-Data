function removeAds(): void {
    // Get all 'li' elements on the page
    const listItems: NodeListOf<HTMLLIElement> = document.querySelectorAll('li');

    listItems.forEach((item: HTMLLIElement) => {
        // Check for the presence of a sponsored indicator
        const isSponsored: Element | null = item.querySelector('.css-16lshh0');

        // If a sponsored indicator is found, remove the 'li' element
        if (isSponsored) {
            item.remove();
        }
    });
}