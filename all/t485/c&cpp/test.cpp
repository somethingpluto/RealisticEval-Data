TEST_CASE("Test prepare_query function") {
    SECTION("Valid named parameters") {
        std::string sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        std::map<std::string, std::string> parameters = {
            {"user_id", "42"},
            {"status", "active"}
        };
        std::string expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        std::vector<std::string> expected_values = {"42", "active"};

        auto [new_sql, value_list] = prepare_query(sql_query, parameters);
        REQUIRE(new_sql == expected_sql);
        REQUIRE(value_list == expected_values);
    }

    SECTION("Missing parameters") {
        std::string sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        std::map<std::string, std::string> parameters = {
            {"user_id", "42"}
        };
        std::string expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        std::vector<std::string> expected_values = {"42"};

        auto [new_sql, value_list] = prepare_query(sql_query, parameters);
        REQUIRE(new_sql == expected_sql);
        REQUIRE(value_list == expected_values);
    }

    SECTION("No parameters") {
        std::string sql_query = "SELECT * FROM users";
        std::map<std::string, std::string> parameters = {};
        std::string expected_sql = "SELECT * FROM users";
        std::vector<std::string> expected_values = {};

        auto [new_sql, value_list] = prepare_query(sql_query, parameters);
        REQUIRE(new_sql == expected_sql);
        REQUIRE(value_list == expected_values);
    }

    SECTION("Multiple same parameters") {
        std::string sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $user_id";
        std::map<std::string, std::string> parameters = {
            {"user_id", "42"}
        };
        std::string expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $1";
        std::vector<std::string> expected_values = {"42"};

        auto [new_sql, value_list] = prepare_query(sql_query, parameters);
        REQUIRE(new_sql == expected_sql);
        REQUIRE(value_list == expected_values);
    }

    SECTION("Special characters in parameters") {
        std::string sql_query = "INSERT INTO users (name, email) VALUES ($name, $email)";
        std::map<std::string, std::string> parameters = {
            {"name", "John Doe"},
            {"email", "john.doe@example.com"}
        };
        std::string expected_sql = "INSERT INTO users (name, email) VALUES ($1, $2)";
        std::vector<std::string> expected_values = {"John Doe", "john.doe@example.com"};

        auto [new_sql, value_list] = prepare_query(sql_query, parameters);
        REQUIRE(new_sql == expected_sql);
        REQUIRE(value_list == expected_values);
    }
}