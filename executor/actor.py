from executor.ccpp_executor import CCPPExecutor
from executor.javascript_executor import JavaScriptExecutor
from executor.python_executor import PythonExecutor
from executor.typescript_executor import TypeScriptExecutor
from executor.java_executor import JavaExecutor


class Actor:
    def __init__(self, task_id, language):
        self.task_id = task_id
        self.language = language
        self.language_suffix_map = {
            "python": "py",
            "javascript": "js",
            "typescript": "ts",
            "c&cpp": "cpp",
            "java": "java"
        }
        self.language_executor_map = {}
        self._init_executor()

    def _init_executor(self):
        self.language_executor_map["python"] = PythonExecutor(type="pass1")
        self.language_executor_map["javascript"] = JavaScriptExecutor(type="pass1")
        self.language_executor_map["typescript"] = TypeScriptExecutor(type="pass1")
        self.language_executor_map["c&cpp"] = CCPPExecutor(type="pass1")
        self.language_executor_map["java"] = JavaExecutor(type="pass1")

    def execute(self):
        if LANGUAGE == "java":
            answer_file_path = f"../all/t{TASK_ID}/java/Answer.java"
            test_file_path = f"../all/t{TASK_ID}/java/Tester.java"
        else:
            answer_file_path = f"../all/t{self.task_id}/{self.language}/answer.{self.language_suffix_map[self.language]}"
            test_file_path = f"../all/t{self.task_id}/{self.language}/test.{self.language_suffix_map[self.language]}"
        with open(answer_file_path, "r", encoding="utf8") as answer_file:
            code = answer_file.read()
        with open(test_file_path, "r", encoding="utf8") as test_file:
            test_code = test_file.read()

        runner = self._get_executor()
        runner.single_run(code, test_code)

    def _get_executor(self):
        return self.language_executor_map[self.language]


if __name__ == '__main__':
    TASK_ID = "183"
    LANGUAGE = "python"
    actor = Actor(task_id=TASK_ID, language=LANGUAGE)
    actor.execute()
