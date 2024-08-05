import os
import unittest

import numpy as np
from PIL import Image

from total.t10.adapted import generate_difference_visualization


class TestImageDifference(unittest.TestCase):

    def test_difference_output(self):
        # 这需要一个具体的测试环境，此处假设存在两个具体的图片路径和输出目录
        generate_difference_visualization('base_image.jpg', 'comparison_image.jpg', './test_output')
        # 确认输出文件存在
        self.assertTrue(os.path.exists('./test_output/difference-0001.jpg'))

    def test_no_difference(self):
        # 使用两次相同的图片来测试没有差异的情况
        generate_difference_visualization('same_image.jpg', 'same_image.jpg', './test_output')
        # 确认输出文件为全黑（没有差异）
        result_image = Image.open('./test_output/difference-0001.jpg')
        self.assertTrue(np.array(result_image).sum() == 0)

    def test_threshold_effect(self):
        # 测试不同阈值对结果的影响
        generate_difference_visualization('base_image.jpg', 'slightly_different_image.jpg', './test_output', visibility_threshold=50)
        # 分析结果，此处假设有具体的期望值
        result_image = Image.open('./test_output/difference-0001.jpg')
        # 检查是否某些像素点的差异被正确忽略
        self.assertTrue(np.array(result_image).sum() < 1000)  # 假定数值，具体需要根据实际情况调整
