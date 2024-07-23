import unittest
import math

from geometry import Circle, Triangle
from geometry.utils import calculate_area

class TestShape(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=3)
        self.assertAlmostEqual(circle.area_calc(), math.pi * 3 ** 2, places=5)

    def test_circle_error_handler(self):
        values = [-5, 0]
        for value in values:
            with self.assertRaises(ValueError):
                circle = Circle(value)

    def test_triangle_area(self):
        triangle = Triangle(s1=3, s2=5, s3=4)
        self.assertAlmostEqual(triangle.area_calc(), 6.0, places=5)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(s1=3, s2=5, s3=4)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(s1=3, s2=6, s3=4)
        self.assertFalse(triangle.is_right_angle())

    def test_triangle_existence(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(s1=3, s2=8, s3=4)

    def test_triangle_negative_sides(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(s1=-1, s2=3, s3=0)

