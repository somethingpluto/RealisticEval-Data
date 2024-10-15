function arrayBufferToString(buffer) {
    // Create a Uint8Array view of the ArrayBuffer
    const uint8Array = new Uint8Array(buffer);
    
    // Convert the Uint8Array to a string using a TextDecoder
    const decoder = new TextDecoder('utf-8');
    return decoder.decode(uint8Array);
}