import unittest
from tvmazereader import main

class TestMethods(unittest.TestCase):
    
    def test_readerMain(self):
        data = main()
        self.assertEqual(len(data),2)

if __name__ == '__main__':
    unittest.main()