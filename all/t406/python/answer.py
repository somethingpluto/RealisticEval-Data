class Colors:

    @staticmethod
    def red(text: str) -> str:
        """text in red color"""
        return f"\033[91m{text}\033[0m"

    @staticmethod
    def green(text: str) -> str:
        """text in green color"""
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def blue(text: str) -> str:
        """text in blue color"""
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def yellow(text: str) -> str:
        """text in yellow color"""
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def magenta(text: str) -> str:
        """text in magenta color"""
        return f"\033[95m{text}\033[0m"

    @staticmethod
    def cyan(text: str) -> str:
        """text in cyan color"""
        return f"\033[96m{text}\033[0m"
