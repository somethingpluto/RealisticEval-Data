enum LogLevel { DEBUG, INFO, WARNING, ERROR, CRITICAL };

class Logger {
public:
    Logger(const std::string& name, LogLevel level = DEBUG)
        : name(name), level(level) {}

    void log(LogLevel level, const std::string& message) {}

private:
    std::string name;
    LogLevel level;

    std::string logLevelToString(LogLevel level) {
        switch (level) {
            case DEBUG: return "DEBUG";
            case INFO: return "INFO";
            case WARNING: return "WARNING";
            case ERROR: return "ERROR";
            case CRITICAL: return "CRITICAL";
            default: return "UNKNOWN";
        }
    }

    std::string currentDateTime() {}
};