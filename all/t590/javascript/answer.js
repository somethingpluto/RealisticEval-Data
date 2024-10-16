function parseHttpRequestLine(response) {
    // Initialize the result object
    const result = {};

    // Step 1: Find the position of the first line of the response (request line)
    const endOfFirstLine = response.indexOf("\r\n");

    if (endOfFirstLine === -1) {
        // If no valid line break is found, return an empty object
        return result;
    }

    // Step 2: Extract the first line (the request line)
    const requestLine = response.substring(0, endOfFirstLine);

    // Step 3: Split the request line into method, URL, and version
    const lineParts = requestLine.split(' ');

    // Ensure we have the correct number of parts
    if (lineParts.length < 3) {
        return result; // Return empty if parsing fails
    }

    const method = lineParts[0];          // Parse method (e.g., GET, POST)
    const url = lineParts[1];              // Parse URL (e.g., /index.html)
    const httpVersion = lineParts[2];      // Parse HTTP version (e.g., HTTP/1.1)

    // Step 4: Store the parsed information in the result object
    result.method = method;
    result.url = url;
    result.http_version = httpVersion;

    // Step 5: Return the result object
    return result;
}