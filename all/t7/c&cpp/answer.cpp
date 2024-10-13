#include <iostream>
#include <memory>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>

// Define logging levels for convenience
#define SPDLOG_LEVEL_DEBUG 0
#define SPDLOG_LEVEL_INFO 1
#define SPDLOG_LEVEL_WARNING 2
#define SPDLOG_LEVEL_ERROR 3
#define SPDLOG_LEVEL_CRITICAL 4

class Logger {
public:
    Logger(const std::string& name, int level = SPDLOG_LEVEL_DEBUG) {
        // Create logger
        auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
        console_sink->set_pattern("[%H:%M:%S] [%n] [%^%l%$] [file: %s line: %#] - %v");

        // Set level
        switch (level) {
            case SPDLOG_LEVEL_DEBUG:
                console_sink->set_level(spdlog::level::debug);
                break;
            case SPDLOG_LEVEL_INFO:
                console_sink->set_level(spdlog::level::info);
                break;
            case SPDLOG_LEVEL_WARNING:
                console_sink->set_level(spdlog::level::warn);
                break;
            case SPDLOG_LEVEL_ERROR:
                console_sink->set_level(spdlog::level::err);
                break;
            case SPDLOG_LEVEL_CRITICAL:
                console_sink->set_level(spdlog::level::critical);
                break;
            default:
                console_sink->set_level(spdlog::level::debug); // Default to debug
                break;
        }

        // Initialize logger with the sink
        logger_ = std::make_shared<spdlog::logger>(name, console_sink);
        spdlog::register_logger(logger_);
        logger_->flush_on(spdlog::level::trace);
    }

    void log(int level, const std::string& message) {
        switch (level) {
            case SPDLOG_LEVEL_DEBUG:
                logger_->debug(message);
                break;
            case SPDLOG_LEVEL_INFO:
                logger_->info(message);
                break;
            case SPDLOG_LEVEL_WARNING:
                logger_->warn(message);
                break;
            case SPDLOG_LEVEL_ERROR:
                logger_->error(message);
                break;
            case SPDLOG_LEVEL_CRITICAL:
                logger_->critical(message);
                break;
            default:
                logger_->debug(message); // Default to debug
                break;
        }
    }

private:
    std::shared_ptr<spdlog::logger> logger_;
};

int main() {
    Logger logger("MyLogger", SPDLOG_LEVEL_INFO);

    logger.log(SPDLOG_LEVEL_DEBUG, "This is a debug message");
    logger.log(SPDLOG_LEVEL_INFO, "This is an info message");
    logger.log(SPDLOG_LEVEL_WARNING, "This is a warning message");
    logger.log(SPDLOG_LEVEL_ERROR, "This is an error message");
    logger.log(SPDLOG_LEVEL_CRITICAL, "This is a critical message");

    return 0;
}