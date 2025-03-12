
def count_unique_colors(image_path: str) -> int:
    # Load the image using OpenCV
    import cv2
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and count the number of times each one appears
    count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 0:
            count += 1

    # Calculate the number of unique colors in the image
    unique_colors = count // 255

    # Return the number of unique colors
    return unique_colors

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