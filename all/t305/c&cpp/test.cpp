TEST_CASE("SeededRandom", "[SeededRandom]") {
    
    SECTION("generates consistent numbers with the same seed") {
        SeededRandom seededRand1(42);
        SeededRandom seededRand2(42);

        REQUIRE(seededRand1.rand() == Catch::Approx(seededRand2.rand()).epsilon(1e-10));
        REQUIRE(seededRand1.rand() == Catch::Approx(seededRand2.rand()).epsilon(1e-10));
        REQUIRE(seededRand1.rand() == Catch::Approx(seededRand2.rand()).epsilon(1e-10));
    }

    SECTION("generates different numbers with different seeds") {
        SeededRandom seededRand1(42);
        SeededRandom seededRand2(24);

        REQUIRE(seededRand1.rand() != Catch::Approx(seededRand2.rand()).epsilon(1e-10));
    }

    SECTION("returns numbers between 0 and 1") {
        SeededRandom seededRand(123456);

        for (int i = 0; i < 1000; ++i) {
            double randValue = seededRand.rand();
            REQUIRE(randValue >= 0);
            REQUIRE(randValue < 1);
        }
    }

    SECTION("produces different sequences with different seeds") {
        SeededRandom seededRand1(123);
        SeededRandom seededRand2(456);

        std::vector<double> sequence1(5);
        std::vector<double> sequence2(5);

        for (int i = 0; i < 5; ++i) {
            sequence1[i] = seededRand1.rand();
            sequence2[i] = seededRand2.rand();
        }

        REQUIRE(sequence1 != sequence2);
    }

    SECTION("consistent sequence with the same seed over multiple calls") {
        SeededRandom seededRand(987654321);

        std::vector<double> sequence1 = { seededRand.rand(), seededRand.rand(), seededRand.rand() };

        // Re-initialize with the same seed to test consistency
        SeededRandom seededRand2(987654321);
        std::vector<double> sequence2 = { seededRand2.rand(), seededRand2.rand(), seededRand2.rand() };

        REQUIRE(sequence1 == sequence2);
    }
}