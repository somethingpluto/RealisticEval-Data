def fix_indentation(code: str) -> str:
    lines = code.split('\n')
    fixed_lines = []
    indentation_level = 0

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith('def ') or stripped_line.startswith('class '):
            indentation_level += 1
        elif stripped_line.startswith('elif ') or stripped_line.startswith('else:') or stripped_line.startswith('except '):
            indentation_level -= 1

        fixed_lines.append('    ' * indentation_level + stripped_line)

        if stripped_line.endswith(':') and not stripped_line.endswith('except:'):
            indentation_level += 1
        elif stripped_line.endswith(')'):
            indentation_level -= 1

    return '\n'.join(fixed_lines)
import unittest


class TestFixIndentation(unittest.TestCase):

    def test_basic_indentation(self):
        code = (
            "def example_function():\n"
            "print(\"Hello, world!\")\n"
            "if True:\n"
            "print(\"True branch\")\n"
            "else:\n"
            "print(\"False branch\")\n"
            "return\n"
        )
        expected = (
            "def example_function():\n"
            "    print(\"Hello, world!\")\n"
            "    if True:\n"
            "        print(\"True branch\")\n"
            "    else:\n"
            "        print(\"False branch\")\n"
            "    return\n"
        )
        actual = fix_indentation(code)
        self.assertEqual(expected, actual)

    def test_empty_lines(self):
        code = (
            "def example_function():\n"
            "\n"
            "print(\"Hello, world!\")\n"
            "\n"
            "if True:\n"
            "print(\"True branch\")\n"
            "return\n"
        )
        expected = (
            "def example_function():\n"
            "\n"
            "    print(\"Hello, world!\")\n"
            "\n"
            "    if True:\n"
            "        print(\"True branch\")\n"
            "    return\n"
        )
        actual = fix_indentation(code)
        self.assertEqual(expected, actual)

    def test_multiple_statements(self):
        code = (
            "def example_function():\n"
            "print(\"Hello, world!\")\n"
            "if True:\n"
            "print(\"True branch\")\n"
            "print(\"Still in True branch\")\n"
            "return\n"
        )
        expected = (
            "def example_function():\n"
            "    print(\"Hello, world!\")\n"
            "    if True:\n"
            "        print(\"True branch\")\n"
            "        print(\"Still in True branch\")\n"
            "    return\n"
        )
        actual = fix_indentation(code)
        self.assertEqual(expected, actual)

    def test_nested_blocks(self):
        code = (
            "def example_function():\n"
            "if True:\n"
            "if False:\n"
            "print(\"False branch\")\n"
            "else:\n"
            "print(\"Else branch\")\n"
            "return\n"
        )
        expected = (
            "def example_function():\n"
            "    if True:\n"
            "        if False:\n"
            "            print(\"False branch\")\n"
            "        else:\n"
            "            print(\"Else branch\")\n"
            "    return\n"
        )
        actual = fix_indentation(code)
        self.assertEqual(expected, actual)

    def test_no_indentation_needed(self):
        code = (
            "def example_function():\n"
            "    print(\"Already correct\")\n"
            "    if True:\n"
            "        print(\"No change needed\")\n"
        )
        expected = code  # Already correctly indented
        actual = fix_indentation(code)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()