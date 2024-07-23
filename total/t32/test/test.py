import unittest


class TestCRC64Calculator(unittest.TestCase):

    def test_crc64_checksum(self):
        # 样本测试以验证校验和计算
        self.assertEqual(CRC64Calculator.compute_crc64(0x123456789ABCDEF0),
                         CRC64Calculator.compute_crc64(0x123456789ABCDEF0))
        self.assertNotEqual(CRC64Calculator.compute_crc64(0x123456789ABCDEF0),
                            CRC64Calculator.compute_crc64(0x0FEDCBA987654321))

    def test_crc64_consistency(self):
        # 检查一致性；相同输入应总是产生相同输出
        input_value = 0xABCDEF1234567890
        first_run = CRC64Calculator.compute_crc64(input_value)
        second_run = CRC64Calculator.compute_crc64(input_value)
        self.assertEqual(first_run, second_run)
