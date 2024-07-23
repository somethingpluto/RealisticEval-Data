import ctypes

class CRC64Calculator:
    """
    用指定的多项式计算 CRC64 校验和的类。
    """
    POLY64REV = 0xC96C5795D7870F42
    crc_table = []

    @classmethod
    def initialize_table(cls):
        if not cls.crc_table:
            for byte in range(256):
                crc = ctypes.c_uint64(byte).value
                for _ in range(8):
                    if crc & 1:
                        crc = (crc >> 1) ^ cls.POLY64REV
                    else:
                        crc >>= 1
                cls.crc_table.append(ctypes.c_uint64(crc).value)

    @staticmethod
    def update_crc(crc, byte):
        table_index = (crc ^ byte) & 0xFF
        return (CRC64Calculator.crc_table[table_index] ^ (crc >> 8)) & 0xFFFFFFFFFFFFFFFF

    @classmethod
    def compute_crc64(cls, input_value):
        cls.initialize_table()

        if input_value < 0:
            input_value = (1 << 64) + input_value

        crc = 0xFFFFFFFFFFFFFFFF
        input_bytes = input_value.to_bytes(8, 'little')

        for byte in input_bytes:
            crc = cls.update_crc(crc, byte)

        return crc ^ 0xFFFFFFFFFFFFFFFF
