/*
 *   Computes the output index from two given indices in the MultiVector's representation
 *   of the G_n orthonormal basis.
 *
 *   This function interprets the integers as little-endian bitstrings, takes their XOR,
 *   and interprets the result as an integer in little-endian.
 *
 *   Args:
 *       idx_1 (uint64_t): Input index 1.
 *       idx_2 (uint64_t): Input index 2.
 *
 *   Returns:
 *       uint64_t: The computed output index.
 */
uint64_t compute_output_index(uint64_t idx_1, uint64_t idx_2) {}