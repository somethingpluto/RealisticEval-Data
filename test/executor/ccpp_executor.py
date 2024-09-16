import subprocess

from test.executor import config


class CCPPExecutor:
    def __init__(self, model_name):
        self._env_path = config.CCPP_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/solution.cpp", "w", encoding="utf8") as temp_file:
            temp_file.write(code)
            temp_file.flush()
            result = self._execute()
            print(result.stdout)
            if result.stderr:
                print("error：", result.stderr)
            if result.returncode == 0:
                print("success")
            else:
                print("error return code：", result.returncode)

        with open(f"{self._env_path}/answer.cpp", "w", encoding="utf8") as file:
            file.write("#define CATCH_CONFIG_MAIN\n")
            file.write("#include \"./lib/catch.hpp\"\n")
            file.write("#include \"./solution.cpp\"\n")
            file.write(test_code)
            file.flush()

    def _execute(self):
        command = "g++ answer.cpp -o test"
        result = subprocess.run(command, capture_output=True, text=True, timeout=10, shell=True, encoding="utf8")
        return result


if __name__ == '__main__':
    code = "#include <vector>\n\nusing namespace std;\n\nvoid merge_sort(vector<double>& arr, int n) {\n    int left_index = 0, right_index = n - 1;\n    while (left_index <= right_index) {\n        int mid = left_index + (right_index - left_index) / 2;\n        if (arr[mid] < arr[left_index]) {\n            left_index = mid + 1;\n        } else {\n            right_index = mid - 1;\n        }\n    }\n    if (left_index == right_index) {\n        cout << \"Merge sort successful!\" << endl;\n    } else {\n        cout << \"Merge sort failed.\" << endl;\n    }\n}\n\nint main() {\n    vector<double> arr = {1.0, 2.0, 3.0, 4.0, 5.0};\n    int n = arr.size();\n    merge_sort(arr, n);\n    return 0;\n}"
    test_code = "TEST_CASE(\"Merge Sort Test Cases\", \"[merge_sort]\") {\n    SECTION(\"Sorting an empty array\") {\n        std::vector<int> empty_array = {};\n        mergeSort(empty_array, 0, empty_array.size() - 1);\n        REQUIRE(empty_array.empty() == true);\n    }\n\n    SECTION(\"Sorting a single element array\") {\n        std::vector<int> single_element = {1};\n        mergeSort(single_element, 0, single_element.size() - 1);\n        REQUIRE(single_element == std::vector<int>{1});\n    }\n\n    SECTION(\"Sorting a sorted array\") {\n        std::vector<int> sorted_array = {1, 2, 3, 4, 5};\n        mergeSort(sorted_array, 0, sorted_array.size() - 1);\n        REQUIRE(sorted_array == std::vector<int>{1, 2, 3, 2, 5});\n    }\n\n    SECTION(\"Sorting a reverse sorted array\") {\n        std::vector<int> reverse_sorted_array = {5, 4, 3, 2, 1};\n        mergeSort(reverse_sorted_array, 0, reverse_sorted_array.size() - 1);\n        REQUIRE(reverse_sorted_array == std::vector<int>{1, 2, 3, 4, 5});\n    }\n\n    SECTION(\"Sorting an array with random integers\") {\n        std::vector<int> random_array = {38, 27, 43, 3, 9, 82, 10};\n        std::vector<int> expected_sorted_array = {3, 9, 10, 27, 38, 43, 82};\n        mergeSort(random_array, 0, random_array.size() - 1);\n        REQUIRE(random_array == expected_sorted_array);\n    }\n}"
    ccpp_executor = CCPPExecutor("test")
    ccpp_executor.single_run(code, test_code)
