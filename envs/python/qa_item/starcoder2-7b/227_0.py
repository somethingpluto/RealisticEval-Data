from PIL import Image

def count_unique_colors(image_path: str) -> int:
    """
    Count the number of unique colors in an image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        int: The number of unique colors in the image.
    """
    image = Image.open(image_path)
    image = image.convert('RGB')
    colors = image.getcolors()
    return len(colors)
import unittest


class TestCountUniqueColor(unittest.TestCase):

    def test_case1(self):
        picture_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase01.png"
        expected_color_num = 1
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case2(self):
        picture_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase02.png"
        expected_color_num = 2
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case3(self):
        picture_path =r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase03.png"
        expected_color_num = 3
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)
    def test_case4(self):
        picture_path =r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase04.png"
        expected_color_num = 466
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)
if __name__ == '__main__':
    unittest.main()