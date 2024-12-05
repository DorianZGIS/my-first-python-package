import dorianpy
import unittest

class TestHello(unittest.TestCase):

  def test_hello(self):
    self.assertIsNone(dorianpy.hello(), str)