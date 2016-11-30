import unittest
import four

class Test4(unittest.TestCase):

    def test_if_no_name_call_me_Nobody(self):
        self.assertEqual(four.greeter(""), 'Hello, Mr Nobody!')

    def test_if_proper_name_do_the_greet(self):
        self.assertEqual(four.greeter("Olivia"), 'Hello, Olivia!')

    def test_if_input_is_integer_typeerror(self):
        self.assertRaises(TypeError, lambda: four.greeter(123))

    def test_if_input_is_undefines_nameerror(self):
        self.assertRaises(NameError, lambda: four.greeter(potato))

if __name__ == '__main__':
    unittest.main()
