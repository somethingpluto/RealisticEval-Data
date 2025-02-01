/**
 * The incoming thread object is converted into a JSON file, which is represented as a Blob object.
 * 
 * @param {Object} thread - The thread object to be converted.
 * @returns {Blob} A Blob object representing the JSON file.
 */
function convertThreadToJSONFile(thread) {
    // Convert the thread object to a JSON string
    const jsonString = JSON.stringify(thread);

    // Create a Blob object with the JSON string and specify the MIME type
    const blob = new Blob([jsonString], { type: 'application/json' });

    return blob;
}
describe('convertThreadToJSONFile Function Tests', () => {
    test('should return a Blob object for a basic thread object', () => {
        const thread1 = { id: 1, title: "First Thread", content: "This is the first thread." };
        const blob1 = convertThreadToJSONFile(thread1);
        expect(blob1 instanceof Blob).toBe(true);
        expect(blob1.type).toBe("application/json");
    });

    test('should return a Blob object for an empty thread object', () => {
        const thread2 = {};
        const blob2 = convertThreadToJSONFile(thread2);
        expect(blob2 instanceof Blob).toBe(true);
        expect(blob2.size).toBe(2); // "{}" has a size of 2 bytes
    });

    test('should return a Blob object for a thread object with nested objects', () => {
        const thread3 = { id: 2, title: "Second Thread", comments: [{ user: "Alice", comment: "Great post!" }] };
        const blob3 = convertThreadToJSONFile(thread3);
        expect(blob3 instanceof Blob).toBe(true);
    });

    test('should return a Blob object for a thread object with special characters', () => {
        const thread4 = { id: 3, title: "Thread & Special <Characters>", content: 'This is a thread with special characters: <, >, &, ".' };
        const blob4 = convertThreadToJSONFile(thread4);
        expect(blob4 instanceof Blob).toBe(true);
    });

    test('should return a Blob object for a thread object with arrays', () => {
        const thread5 = { id: 4, title: "Thread with Array", tags: ["JavaScript", "JSON", "Blob"] };
        const blob5 = convertThreadToJSONFile(thread5);
        expect(blob5 instanceof Blob).toBe(true);
    });
});
