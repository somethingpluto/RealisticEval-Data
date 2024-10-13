package org.real.temp;

public class Answer {

    /**
     * Computes and returns the size of an object in bytes.
     * Note: In Java, there's no direct equivalent to Python's sys.getsizeof() for general objects.
     * This method provides a simplified version that works for primitive types.
     *
     * @param obj The object to measure the memory size of. Currently supports only primitive types.
     * @return The size of the object in bytes.
     */
    public static long sizeInBytes(Object obj) {
        if (obj instanceof Integer) {
            return Integer.SIZE / Byte.SIZE;
        } else if (obj instanceof Long) {
            return Long.SIZE / Byte.SIZE;
        } else if (obj instanceof Float) {
            return Float.SIZE / Byte.SIZE;
        } else if (obj instanceof Double) {
            return Double.SIZE / Byte.SIZE;
        } else if (obj instanceof Boolean) {
            return Boolean.SIZE / Byte.SIZE;
        } else if (obj instanceof Character) {
            return Character.SIZE / Byte.SIZE;
        } else if (obj instanceof Short) {
            return Short.SIZE / Byte.SIZE;
        } else if (obj instanceof Byte) {
            return Byte.SIZE / Byte.SIZE;
        }
        // For non-primitive types or complex objects, we can't compute the size directly.
        return -1; // Indicate unsupported type.
    }
}