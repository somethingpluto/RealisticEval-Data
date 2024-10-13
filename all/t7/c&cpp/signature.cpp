// Define logging levels for convenience
#define SPDLOG_LEVEL_DEBUG spdlog::level::debug
#define SPDLOG_LEVEL_INFO spdlog::level::info
#define SPDLOG_LEVEL_WARNING spdlog::level::warn
#define SPDLOG_LEVEL_ERROR spdlog::level::err
#define SPDLOG_LEVEL_CRITICAL spdlog::level::critical

/**
 * Logger class for logging messages.
 */
class Logger {
public:
    /**
     * Initializes a new logger instance.
     *
     * @param name Name of the logger, typically __name__ to reference the module name.
     * @param level Logging level, default is DEBUG.
     */
    Logger(const std::string& name, int level = SPDLOG_LEVEL_DEBUG) {
    }

    /**
     * Logs a message with the given level.
     *
     * @param level Logging level for the message (e.g., spdlog::level::info).
     * @param message Log message.
     */
    void log(int level, const std::string& message) {
    }

private:
    std::shared_ptr<spdlog::logger> logger_;
};