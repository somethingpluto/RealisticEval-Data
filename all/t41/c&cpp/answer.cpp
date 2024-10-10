#include <iostream>
#include <vector>
#include <bitset>

const int SIZE = 1024;
const int HASH_COUNT = 3;

class BloomFilter {
private:
    std::vector<bool> bitArray;

public:
    BloomFilter() : bitArray(SIZE) {}

    void add(int item) {
        int index1 = item % SIZE;
        int index2 = (item / SIZE) % SIZE;
        int index3 = (item ^ 0x55555555) % SIZE; // XOR operation to get another unique index
        
        bitArray[index1] = true;
        bitArray[index2] = true;
        bitArray[index3] = true;
    }

    bool contains(int item) {
        int index1 = item % SIZE;
        int index2 = (item / SIZE) % SIZE;
        int index3 = (item ^ 0x55555555) % SIZE; // XOR operation to get another unique index
        
        if (!bitArray[index1]) 
            return false;
        if (!bitArray[index2]) 
            return false;
        if (!bitArray[index3]) 
            return false;
        
        return true;
    }
};