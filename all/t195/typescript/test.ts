describe('Stack Test Cases', () => {
    let stack: Stack;

    beforeEach(() => {
        stack = new Stack(10); // Provide capacity when creating the stack
    });

    // Test Case 1: Pushing and popping a single element
    test('push and pop a single element', () => {
        stack.push(3.14);
        expect(stack.pop()).toBeCloseTo(3.14);
        expect(stack.isEmpty()).toBe(true); // Change to isEmpty
    });

    // Test Case 2: Pushing multiple elements and checking peek
    test('push multiple elements and peek', () => {
        stack.push(1.23);
        stack.push(4.56);
        expect(stack.peek()).toBeCloseTo(4.56);
        expect(stack.pop()).toBeCloseTo(4.56);
        expect(stack.pop()).toBeCloseTo(1.23);
        expect(stack.isEmpty()).toBe(true); // Change to isEmpty
    });

    // Test Case 3: Pop from an empty stack (should throw an exception)
    test('pop from an empty stack throws error', () => {
        expect(() => stack.pop()).toThrow(Error);
    });

    // Test Case 4: Peek on an empty stack (should throw an exception)
    test('peek on an empty stack throws error', () => {
        expect(() => stack.peek()).toThrow(Error);
    });

    // Test Case 5: Push elements until stack is full and attempt to push another element
    test('push until full stack throws error', () => {
        const fullStack = new Stack(100); // Provide capacity when creating the stack
        for (let i = 0; i < 100; i++) {
            fullStack.push(i + 0.5);
        }
        expect(() => fullStack.push(100.5)).toThrow(Error);
    });
});