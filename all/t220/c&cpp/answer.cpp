#include <iostream>
#include <deque>
#include <unordered_set>
#include <string>
#include <iterator>
#include <sstream>

class UniqueDeque {
public:
    // Initialize a UniqueDeque object using a deque and an unordered_set.
    UniqueDeque() : _deque(), _set() {}

    // Add an item to the deque if it is not already present.
    bool add(const std::string& item) {
        if (_set.find(item) == _set.end()) {
            _deque.push_back(item);
            _set.insert(item);
            return true;
        }
        return false;
    }

    // Remove an item from the deque if it exists.
    bool deleteItem(const std::string& item) {
        auto it = std::find(_deque.begin(), _deque.end(), item);
        if (it != _deque.end()) {
            _deque.erase(it);
            _set.erase(item);
            return true;
        }
        return false;
    }

    // Check if an item is present in the deque.
    bool contains(const std::string& item) const {
        return _set.find(item) != _set.end();
    }

    // Get the number of elements in the deque.
    size_t size() const {
        return _deque.size();
    }

    // Create an iterator for the deque.
    std::deque<std::string>::iterator begin() {
        return _deque.begin();
    }

    std::deque<std::string>::const_iterator begin() const {
        return _deque.begin();
    }

    std::deque<std::string>::iterator end() {
        return _deque.end();
    }

    std::deque<std::string>::const_iterator end() const {
        return _deque.end();
    }

    // Get a string representation of the UniqueDeque.
    std::string repr() const {
        std::stringstream ss;
        ss << "UniqueDeque([";
        for (auto it = _deque.begin(); it != _deque.end(); ++it) {
            if (it != _deque.begin()) {
                ss << ", ";
            }
            ss << *it;
        }
        ss << "])";
        return ss.str();
    }

private:
    std::deque<std::string> _deque; // Stores elements in order.
    std::unordered_set<std::string> _set; // Ensures uniqueness.
};

int main() {
    UniqueDeque ud;
    ud.add("apple");
    ud.add("banana");
    ud.add("cherry");
    ud.deleteItem("banana");
    std::cout << ud.repr() << std::endl;

    for (const auto& item : ud) {
        std::cout << item << std::endl;
    }

    return 0;
}