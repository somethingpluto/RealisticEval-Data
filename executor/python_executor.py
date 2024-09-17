import json
import os.path

import pandas as pd

import config
import subprocess
from tqdm import tqdm


class PythonExecutor:
    def __init__(self, model_name):
        self._env_path = config.PYTHON_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/temp.test.js", "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.flush()
        result = self._execute(f"{self._env_path}/temp.js")
        if result.stderr:
            print("error：", result.stderr)
        if result.returncode == 0:
            print("success")
        else:
            print("error return code：", result.returncode)

    def batch_run(self, file_path):
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            result_list = json.load(file)

        for item in tqdm(result_list):
            try:
                test_code = item['test_code']

                answer_list = item["answer_list"]
                for index, answer in enumerate(answer_list):
                    code = answer['code']
                    if code == None or code == "":
                        continue
                    with open(f"{self._env_path}/temp.py", "w", encoding="utf8") as file:
                        file.write(code)
                        file.write("\n")
                        file.write(test_code)
                        file.write("\n")
                        file.write("if __name__ == '__main__':")
                        file.write("    unittest.main()")
                        file.flush()
                    result = self._execute(f"{self._env_path}/temp.py")
                    item["result_return_code"] = result.returncode
                    item["stderr"] = result.stderr
                    item["stdout"] = result.stdout
                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_csv(f"../result/{self.model_name}_python.csv")

    def _execute(self, file_path):
        abs_path = os.path.abspath(file_path)
        commands = [r"D:\sdk\python\venvs\realisticeval\Scripts\python.exe", abs_path]
        result = subprocess.run(commands, capture_output=True, text=True, timeout=10, encoding="utf8")
        return result


if __name__ == '__main__':
    code = "import math\n\ndef calculate_distance(agent1: str, agent2: str, observations: dict) -> float:\n    \"\"\"\n    Calculates the Euclidean distance between two agents based on their coordinates in the observations.\n\n    Args:\n        agent1 (str): String representation of agent1's identifier.\n        agent2 (str): String representation of agent2's identifier.\n        observations (dict): Dictionary containing observation question with agent identifiers as keys.Each value is a dictionary with 'x' and 'y' keys representing coordinates.\n\n    Returns:\n        float: Euclidean distance between the two agents.\n    \"\"\"\n    # Get the coordinates of agent1 and agent2\n    agent1_coords = observations[agent1]\n    agent2_coords = observations[agent2]\n\n    # Calculate the Euclidean distance\n    distance = math.sqrt((agent1_coords['x'] - agent2_coords['x'])**2 + (agent1_coords['y'] - agent2_coords['y'])**2)\n\n    return distance"

    test_code = "import unittest\n\nimport numpy as np\n\n\nclass TestCalculateDistance(unittest.TestCase):\n\n    def test_same_point(self):\n        # Both agents are at the same point\n        observations = {\n            \"agent1\": {\"x\": 0, \"y\": 0},\n            \"agent2\": {\"x\": 0, \"y\": 0}\n        }\n        self.assertAlmostEqual(calculate_distance(\"agent1\", \"agent2\", observations), 0.0)\n\n    def test_horizontal_distance(self):\n        # Agents are horizontally apart\n        observations = {\n            \"agent1\": {\"x\": 0, \"y\": 0},\n            \"agent2\": {\"x\": 3, \"y\": 0}\n        }\n        self.assertAlmostEqual(calculate_distance(\"agent1\", \"agent2\", observations), 3.0)\n\n    def test_vertical_distance(self):\n        # Agents are vertically apart\n        observations = {\n            \"agent1\": {\"x\": 0, \"y\": 0},\n            \"agent2\": {\"x\": 0, \"y\": 4}\n        }\n        self.assertAlmostEqual(calculate_distance(\"agent1\", \"agent2\", observations), 4.0)\n\n    def test_diagonal_distance(self):\n        # Agents are diagonally apart\n        observations = {\n            \"agent1\": {\"x\": 1, \"y\": 2},\n            \"agent2\": {\"x\": 4, \"y\": 6}\n        }\n        expected_distance = np.sqrt((4 - 1) ** 2 + (6 - 2) ** 2)\n        self.assertAlmostEqual(calculate_distance(\"agent1\", \"agent2\", observations), expected_distance)\n\n    def test_negative_coordinates(self):\n        # Agents have negative coordinates\n        observations = {\n            \"agent1\": {\"x\": -1, \"y\": -1},\n            \"agent2\": {\"x\": -4, \"y\": -5}\n        }\n        expected_distance = np.sqrt((-4 + 1) ** 2 + (-5 + 1) ** 2)\n        self.assertAlmostEqual(calculate_distance(\"agent1\", \"agent2\", observations), expected_distance)"

    python_executor = PythonExecutor("Meta-Llama-3.1-8B-Instruct")
    # python_executor.single_run(code, test_code)
    python_executor.batch_run(
        "E:\code\code_back\python_project\llm\qa\Meta-Llama-3.1-8B-Instruct_answer\python_answer.json")
