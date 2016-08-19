import unittest
from my_sum_calc import *
class MysumTest(unittest.TestCase):
        def test_my_sum(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(10, 7), 17, 'right but wrong numbers only')
        def test_my_sum_with_non_numbers(self):
                x, y = 2, 'string'
                self.assertEqual(my_sum(x, y), self.assertRaises(TypeError) , 'your test dint pass correct')
        
        def test_my_wrong_sum(self):
                x, y = 2, 'string'
                self.assertEqual(my_wrong_sum(10, 7), 17, 'wrong numbers only') # Functioncall, Expected Answer, Error Message

        def test_my_wrong_sum_with_non_numbers(self):
                 self.assertEqual(my_wrong_sum(x, y), self.assertRaises(TypeError) , 'your test dint pass')
                
if __name__ == '__main__':
    unittest.main()
