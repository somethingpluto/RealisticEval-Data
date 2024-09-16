import unittest


class TestCountUniqueColor(unittest.TestCase):

    def test_case1(self):
        picture_path = "./picture1_2_color.png"
        expected_color_num = 2
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case2(self):
        picture_path = "./picture2_1_color.png"
        expected_color_num = 1
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case3(self):
        picture_path = "./picture3_2_color.png"
        expected_color_num = 31
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case4(self):
        picture_path = "./picture4_5_color.png"
        expected_color_num = 524
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)
