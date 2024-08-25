import ast

code = f"""class TestSmartConvert(unittest.TestCase):
    def test_convert_integer(self):
        self.assertEqual(numerical_str_convert("123"), 123, "Should convert to integer")

    def test_convert_float(self):
        self.assertEqual(numerical_str_convert("123.45"), 123.45, "Should convert to float")

    def test_convert_non_numeric_string(self):
        self.assertEqual(numerical_str_convert("abc"), "abc", "Should remain a string")

    def test_convert_negative_integer(self):
        self.assertEqual(numerical_str_convert("-456"), -456, "Should convert to negative integer")

    def test_convert_negative_float(self):
        self.assertEqual(numerical_str_convert("-456.78"), -456.78, "Should convert to negative float")"""


class TestVisitor(ast.NodeVisitor):
    def __init__(self):
        self.tests = []

    def visit_FunctionDef(self, node):
        # 只收集以 'test' 开头的函数
        if node.name.startswith('test'):
            self.tests.append((node.name, ast.get_source_segment(code, node)))


# 解析代码字符串
parsed_code = ast.parse(code)

# 创建访问者实例并遍历 AST
visitor = TestVisitor()
visitor.visit(parsed_code)

# 输出结果
for test_name, source in visitor.tests:
    print(f"Name: {test_name}\nSource:\n{source}\n")
