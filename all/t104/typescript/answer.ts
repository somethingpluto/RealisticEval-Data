function convertThreadToJSONFile(thread: object): Blob {
    const jsonString: string = JSON.stringify(thread);  // Convert the thread object to a JSON string
    const jsonBlob: Blob = encodeStringAsBlob(jsonString);  // Encode the JSON string as a Blob
    return jsonBlob;
}