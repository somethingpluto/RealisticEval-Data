from typing import List

language_path_map = {
    "python": "../../total_python",
    "java": "../../total_java2",
    "javascript": "../../total_javascript",
    "typescript": "../../total_typescript",
    "c&cpp": "../../total_c&cpp",
    "all": "all"
}


class DataLoader:
    def __init__(self, language: str, ids: List[int]):
        self.language = language.lower()
        self.project_path = self._check_language()

    def _check_language(self) -> str:
        p = language_path_map.get(self.language, None)
        if not p:
            raise ValueError("please check your language")
        return p
