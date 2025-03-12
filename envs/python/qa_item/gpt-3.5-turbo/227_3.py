from PIL import Image

def count_unique_colors(image_path: str) -> int:
    image = Image.open(image_path)
    unique_colors = set()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x,y))
            unique_colors.add(pixel)

    return len(unique_colors)
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