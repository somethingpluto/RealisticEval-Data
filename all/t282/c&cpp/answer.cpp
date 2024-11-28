#include <iostream>
#include <vector>

// Function to flatten a multi-dimensional vector into a one-dimensional vector
std::vector<int> flatten_array(const std::vector<std::vector<int>>& multi_dim_array) {
    std::vector<int> flat_list;

    // Helper function to recursively flatten the array
    void flatten(const std::vector<std::vector<int>>& sub_array) {
        for (const auto& item : sub_array) {
            flatten(item);  // Recursively flatten if the current item is a vector
        }
    }

    // Wrapper function to handle the initial call with the main array
    flatten(multi_dim_array);

    // After recursion, append all elements from the nested vectors
    for (const auto& sub_vector : multi_dim_array) {
        for (int element : sub_vector) {
            flat_list.push_back(element);  // Append the non-vector item to the flat_list
        }
    }

    return flat_list;
}