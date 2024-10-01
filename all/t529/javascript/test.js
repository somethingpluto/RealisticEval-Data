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
        const data = {name: "Alice", age: 25};
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
        expect(consoleLogSpy).toHaveBeenCalledWith(`Data successfully saved to ${mockFilePath}`);
    });

    test('should handle empty object', () => {
        const data = {};
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save nested object to JSON file', () => {
        const data = {user: {name: "Bob", age: 30}, active: true};
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save array of objects to JSON file', () => {
        const data = [
            {product: {id: 1, name: "Laptop", price: 999.99}, inStock: true},
            {product: {id: 2, name: "Phone", price: 499.99}, inStock: false}
        ];
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });

    test('should save object with mixed data types to JSON file', () => {
        const data = {title: "Shopping List", items: ["Milk", "Eggs", "Bread"], total: 3.50, completed: false};
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
                        contact: {email: "alice@techcorp.com", phone: "123-456-7890"}
                    },
                    {id: 2, name: "Bob", role: "Designer", contact: {email: "bob@techcorp.com", phone: "098-765-4321"}}
                ]
            },
            established: 2010
        };
        saveAsJSON(data, mockFilePath);
        const savedData = fs.readFileSync(mockFilePath, 'utf8');
        expect(savedData).toBe(JSON.stringify(data, null, 2));
    });
});