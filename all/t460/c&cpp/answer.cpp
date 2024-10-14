#include <vector>
#include <stdexcept>

std::vector<float> matrix_vector_multiplication(const std::vector<std::vector<float>>& matrix, const std::vector<float>& vector) {
    if (matrix[0].size() != vector.size()) {
        throw std::invalid_argument("Matrix and vector dimensions do not match.");
    }

    std::vector<float> result(vector.size());

    for (int i = 0; i < vector.size(); ++i) {
        for (int j = 0; j < matrix.size(); ++j) {
            result[i] += matrix[j][i] * vector[j];
        }
    }

    return result;
}
```

And here's the equivalent C code using pointers and dynamic memory allocation:

```C
#include <stdlib.h>
#include <string.h>

float* matrix_vector_multiplication(float** matrix, int rows, float* vector, int cols) {
    if (cols != 1) {
        fprintf(stderr, "Vector must be a column vector.\n");
        exit(1);
    }

    float* result = malloc(sizeof(float) * rows);

    for (int i = 0; i < rows; ++i) {
        result[i] = 0;

        for (int j = 0; j < cols; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}

void free_result(float* result) {
    free(result);
}