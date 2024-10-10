#include <iostream>
#include <unordered_set>
#include <deque>

class UniqueDeque {
private:
    std::unordered_set<int> set;
    std::deque<int> deque;

public:
    bool add(int item) {
        if (set.find(item) != set.end()) {
            return false; // Item already present
        }
        set.insert(item);
        deque.push_back(item);
        return true;
    }

    bool deleteItem(int item) {
        auto it = set.find(item);
        if (it == set.end()) {
            return false; // Item not found
        }
        set.erase(it);
        deque.erase(std::remove(deque.begin(), deque.end(), item), deque.end());
        return true;
    }

    bool contains(int item) const {
        return set.find(item) != set.end();
    }

    size_t length() const {
        return set.size();
    }

    void print() const {
        for (const auto &item : deque) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }
};