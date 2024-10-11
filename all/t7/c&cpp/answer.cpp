#include <iostream>
#include <string>
#include <ctime>
#include <fstream>

enum LogLevel { DEBUG, INFO, WARNING, ERROR, CRITICAL };

class Logger {
public:
    Logger(const std::string& name, LogLevel level = DEBUG)
        : name(name), level(level) {}

    void log(LogLevel level, const std::string& message) {
        if (level >= this->level) {
            std::cout << currentDateTime() << " - " << logLevelToString(level)
                      << " - " << name << " - " << message << std::endl;
        }
    }

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

    std::string currentDateTime() {
        std::time_t now = std::time(nullptr);
        char buf[20];
        std::strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", std::localtime(&now));
        return std::string(buf);
    }
};