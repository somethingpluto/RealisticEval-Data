#include <vector>

std::vector<std::vector<int>> createMatrix(int rows, int columns, int initialValue) {
    std::vector<std::vector<int>> matrix(rows, std::vector<int>(columns, initialValue));
    return matrix;
}