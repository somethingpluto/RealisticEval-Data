import * as fs from 'fs';
import * as path from 'path';

/**
 * Converts the data object to JSON format and saves it to the specified file path.
 * @param {Object} data - The data object to be converted to JSON.
 * @param {string} outputFilePath - The file path where the JSON will be saved.
 * @throws Will throw an error if the file path is invalid or the file cannot be written.
 */
function saveAsJSON(data: object, outputFilePath: string): void {
  if (!path.isAbsolute(outputFilePath)) {
    throw new Error('Output file path must be absolute.');
  }

  const resolvedPath = path.resolve(outputFilePath);
  const dir = path.dirname(resolvedPath);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  const jsonData = JSON.stringify(data, null, 2);
  fs.writeFileSync(resolvedPath, jsonData);
}
describe('saveAsJSON', () => {
    const mockFilePath = 'test.json';
    const consoleLogSpy = jest.spyOn(console, 'log').mockImplementation();
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation();

    afterEach(() => {
        // Clean up after each test
        jest.clearAllMocks();
        if (fs.existsSync(mockFilePath)) {
            fs.unlinkSync(mockFilePath); // Remove test file if it exists
        }
    });

    test('should save valid object to JSON file', () => {
        const data = { name: "Alice", age: 25 };
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should handle empty object', () => {
        const data = {};
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save nested object to JSON file', () => {
        const data = { user: { name: "Bob", age: 30 }, active: true };
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save array of objects to JSON file', () => {
        const data = [
            { product: { id: 1, name: "Laptop", price: 999.99 }, inStock: true },
            { product: { id: 2, name: "Phone", price: 499.99 }, inStock: false }
        ];
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save object with mixed data types to JSON file', () => {
        const data = { title: "Shopping List", items: ["Milk", "Eggs", "Bread"], total: 3.50, completed: false };
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save deeply nested object to JSON file', () => {
        const data = {
            company: {
                name: "TechCorp",
                employees: [
                    {
                        id: 1,
                        name: "Alice",
                        role: "Developer",
                        contact: { email: "alice@techcorp.com", phone: "123-456-7890" }
                    },
                    { id: 2, name: "Bob", role: "Designer", contact: { email: "bob@techcorp.com", phone: "098-765-4321" } }
                ]
            },
            established: 2010
        };
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });
});
