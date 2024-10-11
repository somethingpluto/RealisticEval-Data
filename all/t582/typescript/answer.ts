/**
 * Converts an object to a query string.
 *
 * @param {Record<string, any>} params - The parameters to convert.
 * @returns {string} - The query string.
 */
function toQueryString(params: Record<string, any>): string {
    const queryParts: string[] = [];

    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const value = params[key];
            // Check for null/undefined values
            if (value !== null && value !== undefined) {
                // Encode the key and value, then add to the array
                queryParts.push(`${encodeURIComponent(key)}=${encodeURIComponent(value)}`);
            }
        }
    }

    return queryParts.length > 0 ? '?' + queryParts.join('&') : '';
}
