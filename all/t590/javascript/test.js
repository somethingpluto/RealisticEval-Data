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