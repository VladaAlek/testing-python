import unittest
from evens import even_number_of_evens

class TesteEvens(unittest.TestCase):
    
    '''def test_function_returns_True(self):
        self.assertTrue(even_number_of_even)
'''
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_even, 4)

    def test_throws_error_if_the_list_is_empty(self):
        self.assertEqual(even_number_of_even([]), False)
        self.assertEqual(even_number_of_even([2, 4]), True)
        self.assertEqual(even_number_of_even([2]), False)
        self.assertEqual(even_number_of_even([1, 3, 5]), False)

        
    
    
    if __name__ == '__main__':
        unittest.main()