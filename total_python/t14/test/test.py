import unittest
from unittest.mock import patch

class TestJsonFilePicker(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_pick_json_file(self, mock_print, mock_input):
        directory = '/path/to/directory'
        # 假设 `list_json_reports` 和 `read_json_file` 函数已经有效且适当地被模拟
        # 模拟有两个文件存在，用户选择第二个
        with patch('glob.glob', return_value=[
            '/path/to/directory/report1.json',
            '/path/to/directory/report2.json'
        ]), patch('os.path.join', return_value='/path/to/directory/*report*.json'):
            content = pick_json_file(directory)
            mock_print.assert_called_with("请选择一个要加载的 JSON 文件：")
            self.assertIsNotNone(content)
