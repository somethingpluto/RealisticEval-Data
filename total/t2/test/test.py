import unittest
from io import StringIO
from unittest.mock import patch

from total.t2.adapted import manage_software_installation


class TestSoftwareInstallationManager(unittest.TestCase):
    @patch('builtins.input', side_effect=['App1', 'App2', ''])
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='App1\nApp2\n')
    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_process(self, mock_stdout, mock_file, mock_input):
        manage_software_installation()
        self.assertIn("Installation script is ready.", mock_stdout.getvalue())
        file_calls = [call[0][0] for call in mock_file.call_args_list]
        self.assertIn('software_list.txt', file_calls[0])
        self.assertIn('setup_script.ps1', file_calls[1])
        handle = mock_file()
        handle.write.assert_any_call('App1\n')
        handle.write.assert_any_call('App2\n')
        handle.write.assert_any_call('    "App1",\n')
        handle.write.assert_any_call('    "App2",\n')
