JAVA_RUN_ENV = "../envs/java/src"


class JavaExecutor:
    def __init__(self, model_name):
        self._env_path = JAVA_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open("../envs/java/src/main/java/org/real/temp/TempFunc.java","w",encoding="utf8") as code_file:
            code_file.write("package org.real.temp;\n")
            code_file.write("public class TempFunc {\n")
            code_file.write(code)
            code_file.write()
            code_file.flush()