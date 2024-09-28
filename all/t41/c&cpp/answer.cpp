#include <iostream>
#include <string>
#include <vector>
#include <openssl/sha.h> // For SHA-256 hashing
#include <bitset>

class BloomFilter {
public:
    BloomFilter(size_t size, int hash_count)
        : size(size), hash_count(hash_count), bit_array(size) {}

    void add(const std::string& item) {
        // Add an item to the bloom filter
        for (auto hash_value : hashes(item)) {
            bit_array[hash_value] = true;
        }
    }

    bool contains(const std::string& item) const {
        // Implement the "in" functionality
        for (auto hash_value : hashes(item)) {
            if (!bit_array[hash_value]) return false;
        }
        return true;
    }

private:
    size_t size;
    int hash_count;
    std::vector<bool> bit_array;

    std::vector<size_t> hashes(const std::string& item) const {
        // Generate multiple hash values for an item
        std::vector<size_t> hash_values;
        std::string current_item = item;

        for (int i = 0; i < hash_count; ++i) {
            unsigned char hash[SHA256_DIGEST_LENGTH];
            SHA256(reinterpret_cast<const unsigned char*>(current_item.c_str()), current_item.size(), hash);

            // Convert hash to a size_t integer
            size_t hash_result = 0;
            for (int j = 0; j < SHA256_DIGEST_LENGTH; ++j) {
                hash_result = (hash_result * 256 + hash[j]) % size;
            }
            
            hash_values.push_back(hash_result);
            current_item += static_cast<char>(i); // Change item slightly for distinct hash function
        }

        return hash_values;
    }
};

int main() {
    BloomFilter bloomFilter(1000, 3);
    bloomFilter.add("hello");
    bloomFilter.add("world");

    std::cout << "Contains 'hello': " << bloomFilter.contains("hello") << std::endl;
    std::cout << "Contains 'world': " << bloomFilter.contains("world") << std::endl;
    std::cout << "Contains 'unknown': " << bloomFilter.contains("unknown") << std::endl;

    return 0;
}