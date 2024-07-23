import unittest
import math

from geometry_lib import Circle, Triangle
from geometry_lib.utils import calculate_area

class TestUtils(unittest.TestCase):
    def test_calculate_area(self):
        circle = Circle(radius=3)
        triangle = Triangle(s1=3, s2=5, s3=4)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 3 ** 2, places=5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)
