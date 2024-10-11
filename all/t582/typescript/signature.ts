/**
 * Converts an object to a query string.
 * For example:
 *      input: { search: 'test', page: 1, size: 10 };
 *      output: ?search=test&page=1&size=10
 *
 * @param {Record<string, any>} params - The parameters to convert.
 * @returns {string} - The query string.
 */
function toQueryString(params: Record<string, any>): string {
}