# test_app.py
import unittest
from ap import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 1), -1)

if __name__ == "__main__":
    unittest.main()
