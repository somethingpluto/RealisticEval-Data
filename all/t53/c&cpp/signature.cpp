/**
 * @brief Computes and returns the size of an object in bytes in memory.
 * 
 * @tparam T The type of the object.
 * @param obj The object to measure the memory size of.
 * 
 * @return size_t The size of the object in bytes in memory.
 */

template<typename T>
size_t size_in_bytes(const T& obj) {
    return sizeof(obj);
}
