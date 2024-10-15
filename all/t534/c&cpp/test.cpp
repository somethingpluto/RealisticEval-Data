TEST_CASE("removeElementInArray", "[removeElementInArray]") {
    SECTION("returns the original array when the element is not found") {
        std::vector<int> result = removeElementInArray({1, 2, 3, 4}, 5);
        REQUIRE(result == std::vector<int>({1, 2, 3, 4}));
    }

    SECTION("handles an empty array correctly") {
        std::vector<int> result = removeElementInArray({}, 1);
        REQUIRE(result == std::vector<int>({}));
    }

    SECTION("removes an element from a vector of objects") {
        struct Obj {
            int id;
            bool operator==(const Obj& other) const {
                return id == other.id;
            }
        };
        
        Obj obj1{1}, obj2{2}, obj3{3};
        std::vector<Obj> result = removeElementInArray({obj1, obj2, obj3}, obj2);
        REQUIRE(result == std::vector<Obj>({obj1, obj3}));
    }

    SECTION("does not modify the original array") {
        std::vector<int> originalArray = {1, 2, 3};
        std::vector<int> result = removeElementInArray(originalArray, 2);
        REQUIRE(originalArray == std::vector<int>({1, 2, 3}));
        REQUIRE(result == std::vector<int>({1, 3}));
    }
}