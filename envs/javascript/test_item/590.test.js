/**
 * Parses the first line of an HTTP request response string.
 *
 * This function extracts the HTTP method, request URL, and HTTP version
 * from the given response string. The first line of the response should
 * be formatted as "METHOD URL HTTP/VERSION", followed by a CRLF sequence
 * (carriage return and line feed). If the first line does not conform
 * to this format, the function will return an empty object.
 *
 * @param {string} response - A string containing the HTTP response. It is expected
 *                            to start with a request line that includes the method,
 *                            URL, and HTTP version, ending with CRLF ("\r\n").
 *
 * @return {Object} An object containing three key-value pairs:
 *                  - "method": The HTTP method (e.g., GET, POST).
 *                  - "url": The requested URL (e.g., /index.html).
 *                  - "http_version": The HTTP version (e.g., HTTP/1.1).
 *                  If the request line is malformed or empty, the object may contain
 *                  empty strings or be empty.
 *
 * @note The function does not validate the correctness of the HTTP method,
 *       URL, or version; it only parses the input string.
 */
function parseHttpRequestLine(response) {
    // Check if the response is a string and not empty
    if (typeof response !== 'string' || response.trim() === '') {
        return {};
    }

    // Split the response by the CRLF sequence to get the first line
    const firstLine = response.split('\r\n')[0];

    // Split the first line by spaces to extract method, url, and http version
    const parts = firstLine.split(' ');

    // Check if the first line has the expected number of parts
    if (parts.length !== 3) {
        return {};
    }

    // Destructure the parts array into variables
    const [method, url, httpVersion] = parts;

    // Return an object with the parsed values
    return {
        method: method || '',
        url: url || '',
        http_version: httpVersion || ''
    };
}
describe('parseHttpRequestLine', () => {
    test('Valid POST request line', () => {
        const response = "POST /api/data HTTP/1.1\r\n";
        const parsedInfo = parseHttpRequestLine(response);

        expect(parsedInfo.method).toBe("POST");
        expect(parsedInfo.url).toBe("/api/data");
        expect(parsedInfo.http_version).toBe("HTTP/1.1");
    });

    test('PUT request line', () => {
        const response = "PUT /api/update HTTP/2.0\r\n";
        const parsedInfo = parseHttpRequestLine(response);

        expect(parsedInfo.method).toBe("PUT");
        expect(parsedInfo.url).toBe("/api/update");
        expect(parsedInfo.http_version).toBe("HTTP/2.0");
    });

    test('DELETE request line', () => {
        const response = "DELETE /api/delete HTTP/1.1\r\n";
        const parsedInfo = parseHttpRequestLine(response);

        expect(parsedInfo.method).toBe("DELETE");
        expect(parsedInfo.url).toBe("/api/delete");
        expect(parsedInfo.http_version).toBe("HTTP/1.1");
    });

    test('Malformed request line', () => {
        const response = "INVALID REQUEST LINE\r\n";
        const parsedInfo = parseHttpRequestLine(response);

        expect(Object.keys(parsedInfo).length).toBe(0);  // Expect empty result for malformed request
    });
});
