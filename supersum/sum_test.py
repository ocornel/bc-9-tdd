import unittest
from my_sum_calc import *
class MysumTest(unittest.TestCase):
        def test_my_sum1(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(10, 7), 17, 'sum of 10 and 7 should be 17')
                
        def test_my_sum_with_non_numbers1(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_sum('',''))
                
        def test_my_wrong_sum1(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_wrong_sum(10, 7), 17, 'right but wrong numbers only')
                
        def test_my_wrong_sum_with_non_numbers1(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_wrong_sum('',''))
                
        def test_my_sum2(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(123, 321), 123 + 321, 'sum of 123 and 321 should be 444')
                
        def test_my_sum_with_non_numbers2(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_sum(True,False))
                
        def test_my_wrong_sum2(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_wrong_sum(123, 321), 123 + 321, 'sum of 123 and 321 should be 444')
                
        def test_my_wrong_sum_with_non_numbers2(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_wrong_sum(True,False))
                
         def test_my_sum3(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(-2, 5), 3, 'sum of -2 and 5 should be 3')

        def test_my_sum_with_non_numbers3(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_sum('y',5))

        def test_my_wrong_sum3(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_wrong_sum(-2, 5), 3, 'sum of -2 and 5 should be 3')

        def test_my_wrong_sum_with_non_numbers3(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_wrong_sum('y',5))

        def test_my_sum4(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_sum(-9, 3), 6, 'sum of -9 and 3 should be 6')
        
        def test_my_sum_with_non_numbers4(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_sum('x',"8"))

        def test_my_wrong_sum4(self):
                '''Test our function on the some numbers'''
                self.assertEqual(my_wrong_sum(-9, 3), 6, 'sum of -9 and 3 should be 6')
        
        def test_my_wrong_sum_with_non_numbers4(self):
                x, y = 2, 'string'
                self.assertRaises(TypeError,my_wrong_sum('x',"8")) 

if __name__ == '__main__':
    unittest.main()
