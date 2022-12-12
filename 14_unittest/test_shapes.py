import unittest
from shapes import rectangle, triangle, trapezoid

class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.sideA = 6
        self.sideB = 5


    def test_rectangle_with_correct_value(self):
        result = rectangle(6, 5)
        self.assertEqual(result, 30)

    def test_rectangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            rectangle(self.sideA, 'example string')

    def test_triangle_witch_correct_value(self):
        result = triangle(6, 5)
        self.assertEqual(result, 15)

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(self.sideA, 'example string')

    def test_trapezoid_with_correct_value(self):
        result = trapezoid(6, 5, 4)
        self.assertEqual(result, 22)

    def test_trapezoid_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            trapezoid(self.sideA, 'example string')


    def tearDown(self):
        del self.sideA
        del self.sideB


if __name__ == '__main__':
    unittest.main()