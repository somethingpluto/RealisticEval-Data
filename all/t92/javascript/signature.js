/**
 * Decodes HTML entities in a given HTML string.
 * @param {string} htmlString - The HTML string containing entities to decode.
 * @returns {string} The decoded string with HTML entities converted back to their original characters.
 */
const {JSDOM} = require('jsdom');
const dom = new JSDOM();
const {document} = dom.window;

function replaceHtmlEntities(htmlString) {
}