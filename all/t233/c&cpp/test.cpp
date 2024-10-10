TEST_CASE("Remove comments from a string", "[remove_comments]") {
    REQUIRE(remove_comments("Hello, world! # This is a comment") == "Hello, world!");
    REQUIRE(remove_comments("# This is a comment\nHello, world!") == "\nHello, world!");
    REQUIRE(remove_comments("No comments here!") == "No comments here!");
    REQUIRE(remove_comments("Multiple #comments\n#on multiple lines") == "\n");
    REQUIRE(remove_comments("Comments before newline #should stay") == "Comments before newline ");
    REQUIRE(remove_comments("Comments after newline\n#should be removed") == "Comments after newline\n");
}

TEST_CASE("Edge cases", "[remove_comments]") {
    REQUIRE(remove_comments("") == "");
    REQUIRE(remove_comments("\n") == "\n");
    REQUIRE(remove_comments("#") == "");
    REQUIRE(remove_comments("##") == "#");
    REQUIRE(remove_comments("a#b#c") == "ab#c");
}