import unittest

class TestTDDWorking(unittest.TestCase):
    """This test ensure that Unittest is working properly"""
    
    def test_not_equal_numbers(self):
        ''''''
        n1 = 1
        n2 = 2
        self.assertNotEqual(n1, n2)
    
    def test_number_equals_one(self):
        n = 1
        self.assertEqual(n, 1)

if __name__ == '__main__':
    unittest.main()