TEST_CASE("Method Argument Type Check", "[type-check]") {
    auto lambda_with_args = []() -> void {
        int x = 10;
        double y = 3.14;
        std::cout << "x: " << x << ", y: " << y << std::endl;
    };

    std::vector<std::string> positional_args = {"int", "double"};
    std::vector<std::string> keyword_args = {};
    std::vector<std::string> exclude_params = {};

    REQUIRE(method_arg_type_check(lambda_with_args, positional_args, keyword_args, exclude_params));

    // Example of a failing test
    auto lambda_with_wrong_types = []() -> void {
        std::string x = "hello";
        double y = 3.14;
        std::cout << "x: " << x << ", y: " << y << std::endl;
    };

    REQUIRE_THROWS_AS(method_arg_type_check(lambda_with_wrong_types, positional_args, keyword_args, exclude_params), std::invalid_argument);
}