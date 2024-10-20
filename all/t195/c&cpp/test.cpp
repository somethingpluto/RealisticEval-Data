TEST_CASE("stack_t Test Cases", "[stack_t]") {
    stack_t stack(10); // Provide capacity when creating the stack

    // Test Case 1: Pushing and popping a single element
    stack.push(3.14f);
    REQUIRE(stack.pop() == Approx(3.14f));
    REQUIRE(stack.is_empty() == true); // Change to is_empty

    // Test Case 2: Pushing multiple elements and checking peek
    stack.push(1.23f);
    stack.push(4.56f);
    REQUIRE(stack.peek() == Approx(4.56f));
    REQUIRE(stack.pop() == Approx(4.56f));
    REQUIRE(stack.pop() == Approx(1.23f));
    REQUIRE(stack.is_empty() == true); // Change to is_empty

    // Test Case 3: Pop from an empty stack (should throw an exception)
    REQUIRE_THROWS_AS(stack.pop(), std::underflow_error);

    // Test Case 4: Peek on an empty stack (should throw an exception)
    REQUIRE_THROWS_AS(stack.peek(), std::underflow_error);

    // Test Case 5: Push elements until stack is full and attempt to push another element
    stack_t fullStack(100); // Provide capacity when creating the stack
    for (int i = 0; i < 100; ++i) {
        fullStack.push(static_cast<float>(i) + 0.5f);
    }
    REQUIRE_THROWS_AS(fullStack.push(100.5f), std::overflow_error);
}