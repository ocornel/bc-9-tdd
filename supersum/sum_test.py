import unittest
from my_sum_calc import *
class MysumTest(unittest.TestCase):
        def test_my_sum(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(10, 7), 17, 'sum of 10 and 7 should be 17')
                self.assertEqual(my_sum(123, 321), 123 + 321, 'sum of 123 and 321 should be 444')
                self.assertEqual(my_sum(-2, 5), 3, 'sum of -2 and 5 should be 3')
                self.assertEqual(my_sum(-9, 3), 6, 'sum of -9 and 3 should be 6')
        def test_my_sum_with_non_numbers(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_sum('',''))
                self.assertRaises(TypeError,my_sum(True,False))
                self.assertRaises(TypeError,my_sum('y',5))
                self.assertRaises(TypeError,my_sum('x',"8"))

        def test_my_wrong_sum(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_wrong_sum(10, 7), 17, 'right but wrong numbers only')
                self.assertEqual(my_wrong_sum(123, 321), 123 + 321, 'sum of 123 and 321 should be 444')
                self.assertEqual(my_wrong_sum(-2, 5), 3, 'sum of -2 and 5 should be 3')
                self.assertEqual(my_wrong_sum(-9, 3), 6, 'sum of -9 and 3 should be 6')
        def test_my_wrong_sum_with_non_numbers(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_wrong_sum('',''))
                self.assertRaises(TypeError,my_wrong_sum(True,False))
                self.assertRaises(TypeError,my_wrong_sum('y',5))
                self.assertRaises(TypeError,my_wrong_sum('x',"8"))
        
if __name__ == '__main__':
    unittest.main()
