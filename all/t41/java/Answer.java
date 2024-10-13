package org.real.temp;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.BitSet;

public class Answer {

    public static class BloomFilter {
        private final int size;
        private final int hashCount;
        private final BitSet bitArray;

        public BloomFilter(int size, int hashCount) {
            this.size = size;
            this.hashCount = hashCount;
            this.bitArray = new BitSet(size);
        }

        private Iterable<Integer> hashes(String item) {
            return () -> new java.util.Iterator<>() {
                private int index = 0;

                @Override
                public boolean hasNext() {
                    return index < hashCount;
                }

                @Override
                public Integer next() {
                    if (!hasNext()) {
                        throw new java.util.NoSuchElementException();
                    }
                    byte[] itemBytes = item.getBytes(java.nio.charset.StandardCharsets.UTF_8);
                    try {
                        MessageDigest digest = MessageDigest.getInstance("SHA-256");
                        byte[] hashResult = digest.digest(itemBytes);
                        long hashValue = bytesToLong(hashResult);
                        index++;
                        return (int) (hashValue + index) % size;
                    } catch (NoSuchAlgorithmException e) {
                        throw new RuntimeException(e);
                    }
                }

                private long bytesToLong(byte[] bytes) {
                    long result = 0;
                    for (byte b : bytes) {
                        result = (result << 8) | (b & 0xFF);
                    }
                    return result;
                }
            };
        }

        public void add(String item) {
            for (int hashValue : hashes(item)) {
                bitArray.set(hashValue);
            }
        }

        public boolean contains(String item) {
            for (int hashValue : hashes(item)) {
                if (!bitArray.get(hashValue)) {
                    return false;
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {
        // Example usage
        BloomFilter bloomFilter = new BloomFilter(1000, 5);
        bloomFilter.add("example");
        System.out.println(bloomFilter.contains("example")); // Expected: true
        System.out.println(bloomFilter.contains("not_in_filter")); // Expected: false
    }
}