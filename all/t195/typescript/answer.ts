class Stack {
    private static readonly MAX_SIZE = 100; // Maximum size of the stack
    private stack: number[];                // Array to hold the stack elements
    private top: number;                    // Index of the top element in the stack

    /**
     * @brief Constructor that initializes the stack.
     *
     * The constructor initializes the stack's top index to -1, indicating that the stack is empty.
     */
    constructor() {
        this.stack = new Array(Stack.MAX_SIZE);
        this.top = -1;
    }

    /**
     * @brief Pushes a floating-point number onto the stack.
     *
     * @param value The floating-point number to be pushed onto the stack.
     * @throws Error if the stack is full.
     */
    public push(value: number): void {
        if (this.top >= Stack.MAX_SIZE - 1) {
            throw new Error("Stack overflow: Cannot push onto a full stack.");
        }
        this.stack[++this.top] = value;
    }

    /**
     * @brief Pops the top element off the stack and returns it.
     *
     * @return The floating-point number that was popped from the stack.
     * @throws Error if the stack is empty.
     */
    public pop(): number {
        if (this.top < 0) {
            throw new Error("Stack underflow: Cannot pop from an empty stack.");
        }
        return this.stack[this.top--];
    }

    /**
     * @brief Returns the top element of the stack without removing it.
     *
     * @return The floating-point number at the top of the stack.
     * @throws Error if the stack is empty.
     */
    public peek(): number {
        if (this.top < 0) {
            throw new Error("Stack underflow: Cannot peek on an empty stack.");
        }
        return this.stack[this.top];
    }

    /**
     * @brief Checks whether the stack is empty.
     *
     * @return true if the stack is empty; false otherwise.
     */
    public isEmpty(): boolean {
        return this.top < 0;
    }
}