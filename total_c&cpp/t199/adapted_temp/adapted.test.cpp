#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("BTree Insertion", "[BTree]") {
    BTree tree;
    tree.insert(10, "val10");
    tree.insert(20, "val20");
    tree.insert(5, "val5");

    REQUIRE(tree.search(10) == true);
    REQUIRE(tree.search_values(10) == "val10");

    REQUIRE(tree.search(20) == true);
    REQUIRE(tree.search_values(20) == "val20");

    REQUIRE(tree.search(5) == true);
    REQUIRE(tree.search_values(5) == "val5");
}

TEST_CASE("BTree Search", "[BTree]") {
    BTree tree;
    tree.insert(15, "val15");
    tree.insert(25, "val25");

    REQUIRE(tree.search(15) == true);
    REQUIRE(tree.search_values(15) == "val15");

    REQUIRE(tree.search(25) == true);
    REQUIRE(tree.search_values(25) == "val25");

    REQUIRE(tree.search(10) == false);
    REQUIRE(tree.search_values(10) == "false");
}

TEST_CASE("BTree Remove", "[BTree]") {
    BTree tree;
    tree.insert(30, "val30");
    tree.insert(40, "val40");
    tree.insert(35, "val35");

    tree.remove(35);
    REQUIRE(tree.search(35) == false);
    REQUIRE(tree.search_values(35) == "false");

    REQUIRE(tree.search(30) == true);
    REQUIRE(tree.search_values(30) == "val30");

    REQUIRE(tree.search(40) == true);
    REQUIRE(tree.search_values(40) == "val40");
}

TEST_CASE("BTree Complex Operations", "[BTree]") {
    BTree tree;
    tree.insert(50, "val50");
    tree.insert(60, "val60");
    tree.insert(55, "val55");
    tree.insert(45, "val45");

    REQUIRE(tree.search(55) == true);
    REQUIRE(tree.search_values(55) == "val55");

    tree.remove(60);
    REQUIRE(tree.search(60) == false);
    REQUIRE(tree.search_values(60) == "false");

    REQUIRE(tree.search(50) == true);
    REQUIRE(tree.search_values(50) == "val50");
}

TEST_CASE("BTree Empty Tree Operations", "[BTree]") {
    BTree tree;
    
    REQUIRE(tree.search(100) == false);
    REQUIRE(tree.search_values(100) == "false");

    tree.insert(100, "val100");
    REQUIRE(tree.search(100) == true);
    REQUIRE(tree.search_values(100) == "val100");

    tree.remove(100);
    REQUIRE(tree.search(100) == false);
    REQUIRE(tree.search_values(100) == "false");
}