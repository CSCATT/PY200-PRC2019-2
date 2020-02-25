import unittest
from lab1_2 import glass


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, glass, "200", 100)


if __name__ == '__main__':
    unittest.main()
