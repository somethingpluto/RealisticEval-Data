#include <stdexcept>

/**
 * @brief Implement a floating-point stack structure based on arrays
 *
 * This class provides basic stack operations including push, pop, peek, and checking if the stack is empty.
 * The stack is implemented using a fixed-size array. If the stack reaches its maximum capacity, no more elements
 * can be pushed onto it until space is freed by popping elements.
 */
class FloatStack {
private:
    static const int MAX_SIZE = 100;  // Maximum size of the stack
    float stack[MAX_SIZE];            // Array to hold the stack elements
    int top;                          // Index of the top element in the stack

public:
    /**
     * @brief Constructor that initializes the stack.
     *
     * The constructor initializes the stack's top index to -1, indicating that the stack is empty.
     */
    FloatStack() : top(-1) {}

    /**
     * @brief Pushes a floating-point number onto the stack.
     *
     * @param value The floating-point number to be pushed onto the stack.
     * @throws std::overflow_error if the stack is full.
     */
    void push(float value) {
        if (top >= MAX_SIZE - 1) {
            throw std::overflow_error("Stack overflow: Cannot push onto a full stack.");
        }
        stack[++top] = value;
    }

    /**
     * @brief Pops the top element off the stack and returns it.
     *
     * @return The floating-point number that was popped from the stack.
     * @throws std::underflow_error if the stack is empty.
     */
    float pop() {
        if (top < 0) {
            throw std::underflow_error("Stack underflow: Cannot pop from an empty stack.");
        }
        return stack[top--];
    }

    /**
     * @brief Returns the top element of the stack without removing it.
     *
     * @return The floating-point number at the top of the stack.
     * @throws std::underflow_error if the stack is empty.
     */
    float peek() const {
        if (top < 0) {
            throw std::underflow_error("Stack underflow: Cannot peek on an empty stack.");
        }
        return stack[top];
    }

    /**
     * @brief Checks whether the stack is empty.
     *
     * @return true if the stack is empty; false otherwise.
     */
    bool isEmpty() const {
        return top < 0;
    }
};