import unittest
from challenge import *

class Test(unittest.TestCase):
    def testADD(self):
        self.assertEqual(add(10, 20), 30)
        self.assertNotEqual(add(10, -20), 30)
        self.assertTrue(add(10, 20) == 40)
        self.assertFalse(add(-10, 20) == 30)

    def testSUBTRACT(self):
        self.assertEqual(subtract(50, 20), 30)
        self.assertNotEqual(subtract(-50, -20), 30)
        self.assertTrue(subtract(50, 20) == 30)
        self.assertFalse(subtract(10, 20) == 30)

if __name__ == '__main__':
    unittest.main()
