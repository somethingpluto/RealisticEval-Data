import unittest
import os

from task_code.t6.adapted import process_programs


class TestProcessPrograms(unittest.TestCase):

    def setUp(self):
        self.test_filename = "winget_list.txt"
        self.test_scriptname = "install_apps.ps1"
        self.programs = ["notepad++", "python", "git"]

        # Clear test files if they exist
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_scriptname):
            os.remove(self.test_scriptname)

    def test_append_to_file(self):
        process_programs(["notepad++", "python"])

        with open(self.test_filename, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].strip(), "notepad++")
        self.assertEqual(lines[1].strip(), "python")

    def test_generate_powershell_script(self):
        process_programs(self.programs)

        with open(self.test_scriptname, "r") as script_file:
            content = script_file.read()

        self.assertIn('$programs = @(', content)
        self.assertIn('"notepad++",', content)
        self.assertIn('"python",', content)
        self.assertIn('"git",', content)
        self.assertIn('Start-Process -Wait -FilePath \'winget\' -ArgumentList \'install\', $app', content)

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_scriptname):
            os.remove(self.test_scriptname)