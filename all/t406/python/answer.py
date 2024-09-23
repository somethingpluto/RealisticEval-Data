class Colors:
    # ANSI escape codes for different colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'  # Resets the color to default

    @staticmethod
    def red(text):
        """text in red color"""
        return f"{Colors.RED}{text}{Colors.RESET}"

    @staticmethod
    def green(text):
        """text in green color"""
        return f"{Colors.GREEN}{text}{Colors.RESET}"

    @staticmethod
    def blue(text):
        """text in blue color"""
        return f"{Colors.BLUE}{text}{Colors.RESET}"

    @staticmethod
    def yellow(text):
        """text in yellow color"""
        return f"{Colors.YELLOW}{text}{Colors.RESET}"

    @staticmethod
    def magenta(text):
        """text in magenta color"""
        return f"{Colors.MAGENTA}{text}{Colors.RESET}"

    @staticmethod
    def cyan(text):
        """text in cyan color"""
        return f"{Colors.CYAN}{text}{Colors.RESET}"
