function replaceHtmlEntities(htmlString) { // This function was written by ChatGPT and modified by me (iamsirsammy)
    const doc = new DOMParser().parseFromString(htmlString.replace("&amp;", "&"), 'text/html');
    return doc.documentElement.innerText;
}
  