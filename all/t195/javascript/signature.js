/**
 * Implement a floating-point stack structure based on arrays
 *
 * This class provides basic stack operations including push, pop, peek, and checking if the stack is empty.
 * The stack is implemented using a fixed-size array. If the stack reaches its maximum capacity, no more elements
 * can be pushed onto it until space is freed by popping elements.
 */
class Stack {
    static MAX_SIZE = 100;  // Maximum size of the stack
    stack = new Array(Stack.MAX_SIZE);  // Array to hold the stack elements
    top = -1;  // Index of the top element in the stack

    /**
     * Pushes a floating-point number onto the stack.
     *
     * @param {number} value The floating-point number to be pushed onto the stack.
     * @throws {Error} if the stack is full.
     */
    push(value) {
        if (this.top >= Stack.MAX_SIZE - 1) {
            throw new Error("Stack overflow: Cannot push onto a full stack.");
        }
        this.stack[++this.top] = value;
    }

    /**
     * Pops the top element off the stack and returns it.
     *
     * @return {number} The floating-point number that was popped from the stack.
     * @throws {Error} if the stack is empty.
     */
    pop() {
        if (this.top < 0) {
            throw new Error("Stack underflow: Cannot pop from an empty stack.");
        }
        return this.stack[this.top--];
    }

    /**
     * Returns the top element of the stack without removing it.
     *
     * @return {number} The floating-point number at the top of the stack.
     * @throws {Error} if the stack is empty.
     */
    peek() {
        if (this.top < 0) {
            throw new Error("Stack underflow: Cannot peek on an empty stack.");
        }
        return this.stack[this.top];
    }

    /**
     * Checks whether the stack is empty.
     *
     * @return {boolean} true if the stack is empty; false otherwise.
     */
    isEmpty() {
        return this.top < 0;
    }
}