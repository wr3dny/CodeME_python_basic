import unittest
from shapes import rectangle, triangle, trapeze

class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.sideA = 6
        self.sideB = 5
        self.higth = 4

    def test_trapeze_with_correct_value(self):
        result = trapeze(6, 5, 4)
        self.assertEqual(result, 22)

    def tearDown(self):
        del self.sideA
        del self.sideB


if __name__ == '__main__':
    unittest.main()