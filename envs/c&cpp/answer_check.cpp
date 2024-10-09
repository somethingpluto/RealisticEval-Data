#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}TEST_CASE("Merge Sort Test Cases", "[merge_sort]") {
    SECTION("Sorting an empty array") {
        std::vector<int> empty_array = {};
        merge_sort(empty_array, 0, empty_array.size() - 1);
        REQUIRE(empty_array.empty() == true);
    }

    SECTION("Sorting a single element array") {
        std::vector<int> single_element = {1};
        merge_sort(single_element, 0, single_element.size() - 1);
        REQUIRE(single_element == std::vector<int>{1});
    }

    SECTION("Sorting a sorted array") {
        std::vector<int> sorted_array = {1, 2, 3, 4, 5};
        merge_sort(sorted_array, 0, sorted_array.size() - 1);
        REQUIRE(sorted_array == std::vector<int>{1, 2, 3, 2, 5});
    }

    SECTION("Sorting a reverse sorted array") {
        std::vector<int> reverse_sorted_array = {5, 4, 3, 2, 1};
        merge_sort(reverse_sorted_array, 0, reverse_sorted_array.size() - 1);
        REQUIRE(reverse_sorted_array == std::vector<int>{1, 2, 3, 4, 5});
    }

    SECTION("Sorting an array with random integers") {
        std::vector<int> random_array = {38, 27, 43, 3, 9, 82, 10};
        std::vector<int> expected_sorted_array = {3, 9, 10, 27, 38, 43, 82};
        merge_sort(random_array, 0, random_array.size() - 1);
        REQUIRE(random_array == expected_sorted_array);
    }
}