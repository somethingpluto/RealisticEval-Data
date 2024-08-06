import unittest
from unittest.mock import patch


def get_mock_input(input_values):
    """ Generator to return values for each call to input() """
    for value in input_values:
        yield value


class TestGeneratePowerShellInstallScript(unittest.TestCase):
    def check_script_contents(self, expected_programs):
        """ Helper function to check the contents of the generated PowerShell script """
        script_filename = 'install_programs.ps1'
        with open(script_filename, 'r') as file:
            lines = file.readlines()

        # Check installation lines for programs
        install_lines = [line.strip() for line in lines if line.strip().startswith('choco install')]
        self.assertEqual(len(install_lines), len(expected_programs))
        for program in expected_programs:
            self.assertIn(f"choco install {program} -y", install_lines)

    @patch('builtins.input', side_effect=get_mock_input(["firefox", "done"]))
    def test_single_program(self, mock_input):
        generate_powershell_install_script()
        self.check_script_contents(["firefox"])

    @patch('builtins.input', side_effect=get_mock_input(["nodejs", "python", "git", "done"]))
    def test_multiple_programs(self, mock_input):
        generate_powershell_install_script()
        self.check_script_contents(["nodejs", "python", "git"])

    @patch('builtins.input', side_effect=get_mock_input(["done"]))
    def test_no_programs(self, mock_input):
        generate_powershell_install_script()
        self.check_script_contents([])

    @patch('builtins.input', side_effect=get_mock_input(["NodeJS", "Python3", "done"]))
    def test_case_sensitivity(self, mock_input):
        generate_powershell_install_script()
        self.check_script_contents(["NodeJS", "Python3"])

    @patch('builtins.input', side_effect=get_mock_input(["sql server", "visual studio code", "done"]))
    def test_special_characters(self, mock_input):
        generate_powershell_install_script()
        self.check_script_contents(["sql server", "visual studio code"])
