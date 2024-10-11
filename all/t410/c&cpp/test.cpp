TEST_CASE("Check XOR Sum Function", "[check_xor_sum]") {
    // Initialize numpy array object
    Py_Initialize();
    import_array();

    // Test case 1: Normal scenario with expected result
    np::ndarray arr1 = np::frompyarray(np::array<int>({1, 0, 1}));
    REQUIRE(check_xor_sum(arr1) == true); // Replace with actual expected result

    // Test case 2: Scenario with unexpected result
    np::ndarray arr2 = np::frompyarray(np::array<int>({0, 0, 0}));
    REQUIRE(check_xor_sum(arr2) == false); // Replace with actual expected result

    // Add more test cases as needed

    // Finalize numpy
    Py_Finalize();
}