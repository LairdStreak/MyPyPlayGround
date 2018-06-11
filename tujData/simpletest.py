import unittest

class MyTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(0, 0)

    def test2(self):
        self.assertNotEqual(1,0)


if __name__ == '__main__':
    unittest.main()        