function htmlToMDSyntax(html) { // accounts for an edge case where chatgpt produces both an ordered list and an unordered list when exporting
    let newh =  html
        .replaceAll(`<code>`, '\`')
        .replaceAll(`</code>`, '\`')
        .replaceAll(`<p>`, '\n')
        .replaceAll(`</p>`, '\n')
        .replaceAll(`<h1>`, '# ')
        .replaceAll(`</h1>`, '')
        .replaceAll(`<h2>`, '## ')
        .replaceAll(`</h2>`, '')
        .replaceAll(`<h3>`, '### ')
        .replaceAll(`</h3>`, '');

    let isOrderedList = html.includes('<ol>');
    let isUnorderedList = html.includes('<ul>');

    if (isOrderedList){
        newh = newh
            .replaceAll(`<ol>`, `<ol class="ordered-list">`)
            .replaceAll(`</ol>`, `</ol>`);

        let parser = new DOMParser();
        let doc = parser.parseFromString(newh, 'text/html');
        let orderedListItems = doc.querySelectorAll('.ordered-list li');
        for (let i = 0; i < orderedListItems.length; i++) {
            orderedListItems[i].innerHTML = `${i + 1}. ` + orderedListItems[i].innerHTML;
        }
        newh = doc.body.innerHTML
            .replaceAll(`<ol class="ordered-list">`, "\n")
            .replaceAll(`</ol>`, "\n")
            .replaceAll(`</li>`, "\n")
    }
    if (isUnorderedList){
        newh = newh
            .replaceAll(`<ul>`, `<ul class="unordered-list">`)
            .replaceAll(`</ul>`, `</ul>`);

        let parser = new DOMParser();
        let doc = parser.parseFromString(newh, 'text/html');
        let unorderedListItems = doc.querySelectorAll('.unordered-list li');
        for (let i = 0; i < unorderedListItems.length; i++) {
            unorderedListItems[i].innerHTML = `- ` + unorderedListItems[i].innerHTML;
        }
        newh = doc.body.innerHTML
            .replaceAll(`<ul class="unordered-list">`, "\n")
            .replaceAll(`</ul>`, "\n")
            .replaceAll(`</li>`, "\n")
    }
    newh = newh.replaceAll(`<li>`, "")

    return newh
}