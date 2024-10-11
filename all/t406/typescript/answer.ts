class Colors {
    static red(text: string): string {
        // Implement the logic to return text in red color
        return `\x1b[31m${text}\x1b[0m`;
    }

    static green(text: string): string {
        // Implement the logic to return text in green color
        return `\x1b[32m${text}\x1b[0m`;
    }

    static blue(text: string): string {
        // Implement the logic to return text in blue color
        return `\x1b[34m${text}\x1b[0m`;
    }

    static yellow(text: string): string {
        // Implement the logic to return text in yellow color
        return `\x1b[33m${text}\x1b[0m`;
    }

    static magenta(text: string): string {
        // Implement the logic to return text in magenta color
        return `\x1b[35m${text}\x1b[0m`;
    }

    static cyan(text: string): string {
        // Implement the logic to return text in cyan color
        return `\x1b[36m${text}\x1b[0m`;
    }
}