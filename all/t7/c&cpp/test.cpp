TEST_CASE("TestLogger", "[Logger]") {
    SECTION("Initialization") {
        const std::string logger_name = "TestLogger";
        Logger logger(logger_name);

        REQUIRE(logger.logger_->name() == logger_name);
        REQUIRE(logger.logger_->level() == spdlog::level::debug);
    }

    SECTION("Default Logging Level") {
        const std::string logger_name = "DefaultLogger";
        Logger logger(logger_name);

        REQUIRE(logger.logger_->level() == spdlog::level::debug);
    }

    SECTION("Console Handler Added") {
        const std::string logger_name = "TestLogger";
        Logger logger(logger_name);

        auto handlers = logger.logger_->sinks();
        REQUIRE(handlers.size() > 0);
        REQUIRE(std::dynamic_pointer_cast<spdlog::sinks::stdout_color_sink_mt>(handlers[0]) != nullptr);
    }
}