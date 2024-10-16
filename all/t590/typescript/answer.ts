function parseHttpRequestLine(response: string): Record<string, string> {
    // Initialize the result object
    const result: Record<string, string> = {};

    // Step 1: Find the position of the first line of the response (request line)
    const endOfFirstLine = response.indexOf("\r\n");

    if (endOfFirstLine === -1) {
        // If no valid line break is found, return an empty object
        return result;
    }

    // Step 2: Extract the first line (the request line)
    const requestLine = response.substring(0, endOfFirstLine);

    // Step 3: Split the request line into method, URL, and version
    const lineParts = requestLine.split(/\s+/);
    const method = lineParts[0];
    const url = lineParts[1];
    const httpVersion = lineParts[2];

    // Step 4: Store the parsed information in the result object
    result["method"] = method;
    result["url"] = url;
    result["http_version"] = httpVersion;

    // Step 5: Return the result object
    return result;
}