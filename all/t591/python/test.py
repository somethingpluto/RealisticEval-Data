class Tester(unittest.TestCase):

    def setUp(self):
        self.color = Color()

    def test_rgb_red(self):
        rgb = self.color.getColor(Color.RED)
        self.assertEqual(rgb, (255, 0, 0))

    def test_rgb_green(self):
        rgb = self.color.getColor(Color.GREEN)
        self.assertEqual(rgb, (0, 255, 0))

    def test_rgb_blue(self):
        rgb = self.color.getColor(Color.BLUE)
        self.assertEqual(rgb, (0, 0, 255))

    def test_rgb_yellow(self):
        rgb = self.color.getColor(Color.YELLOW)
        self.assertEqual(rgb, (255, 255, 0))

    def test_rgb_magenta(self):
        rgb = self.color.getColor(Color.MAGENTA)
        self.assertEqual(rgb, (255, 0, 255))

    def test_rgb_cyan(self):
        rgb = self.color.getColor(Color.CYAN)
        self.assertEqual(rgb, (0, 255, 255))

    def test_rgb_white(self):
        rgb = self.color.getColor(Color.WHITE)
        self.assertEqual(rgb, (255, 255, 255))

    def test_rgb_black(self):
        rgb = self.color.getColor(Color.BLACK)
        self.assertEqual(rgb, (0, 0, 0))

    def test_rgb_orange(self):
        rgb = self.color.getColor(Color.ORANGE)
        self.assertEqual(rgb, (255, 165, 0))

    def test_rgb_purple(self):
        rgb = self.color.getColor(Color.PURPLE)
        self.assertEqual(rgb, (128, 0, 128))

    def test_rgb_pink(self):
        rgb = self.color.getColor(Color.PINK)
        self.assertEqual(rgb, (255, 192, 203))

    def test_rgb_brown(self):
        rgb = self.color.getColor(Color.BROWN)
        self.assertEqual(rgb, (165, 42, 42))