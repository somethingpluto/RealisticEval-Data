import unittest
import json
import os
from task_code.t1.adapted import merge_json_list_data


class TestCombineJsonFiles(unittest.TestCase):

    def setUp(self):
        os.makedirs('./input/case1', exist_ok=True)
        os.makedirs('./input/case2', exist_ok=True)
        os.makedirs('./input/case3', exist_ok=True)
        os.makedirs('./output', exist_ok=True)

        with open('./input/case1/file1.json', 'w', encoding='utf8') as f:
            json.dump([{"name": "Alice"}, {"name": "Bob"}], f, indent=4)
        with open('./input/case1/file2.json', 'w', encoding='utf8') as f:
            json.dump([{"name": "Charlie"}, {"name": "David"}], f, indent=4)

        with open('./input/case2/file1.json', 'w', encoding='utf8') as f:
            json.dump([{"name": "Alice"}, {"name": "Bob"}], f, indent=4)
        with open('./input/case2/file2.json', 'w', encoding='utf8') as f:
            json.dump({"name": "Charlie"}, f, indent=4)
        with open('./input/case2/file3.json', 'w', encoding='utf8') as f:
            json.dump([{"name": "David"}], f, indent=4)

    def tearDown(self):
        for root, dirs, files in os.walk('./input'):
            for file in files:
                os.remove(os.path.join(root, file))
        for root, dirs, files in os.walk('./output'):
            for file in files:
                os.remove(os.path.join(root, file))

    def test_case1(self):
        merge_json_list_data('./input/case1', './output/case1_output.json')
        with open('./output/case1_output.json', 'r', encoding='utf8') as file:
            self.assertEqual(json.load(file),
                             [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}, {"name": "David"}],
                             "test case1 failed")

    def test_case2(self):
        merge_json_list_data('./input/case2', './output/case2_output.json')
        with open('./output/case2_output.json', 'r', encoding='utf8') as file:
            self.assertEqual(json.load(file), [{"name": "Alice"}, {"name": "Bob"}, {"name": "David"}],
                             "test case2 failed")

    def test_case3(self):
        merge_json_list_data('./input/case3', './output/case3_output.json')
        with open('./output/case3_output.json', 'r', encoding='utf8') as file:
            self.assertEqual(json.load(file), [], "test case3 failed")
