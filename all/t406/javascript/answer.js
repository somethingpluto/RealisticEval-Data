class Colors {
    static red(text) {
        // text in red color
        return `\x1b[31m${text}\x1b[0m`;
    }

    static green(text) {
        // text in green color
        return `\x1b[32m${text}\x1b[0m`;
    }

    static blue(text) {
        // text in blue color
        return `\x1b[34m${text}\x1b[0m`;
    }

    static yellow(text) {
        // text in yellow color
        return `\x1b[33m${text}\x1b[0m`;
    }

    static magenta(text) {
        // text in magenta color
        return `\x1b[35m${text}\x1b[0m`;
    }

    static cyan(text) {
        // text in cyan color
        return `\x1b[36m${text}\x1b[0m`;
    }
}