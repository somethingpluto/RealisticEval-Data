/**
 * Decompose a flat index `n` into a multidimensional index based on the given shape.
 *
 * @param n - Flat index (non-negative integer).
 * @param shape - Tuple representing the dimensions of the multi-dimensional array.
 * @returns A tuple representing the multidimensional index corresponding to `n`.
 * @throws {Error} If `n` is out of bounds for the array defined by `shape`.
 */
function decompose(n: number, shape: number[]): [number, ...number[]] {}