import unittest
from unittest.mock import MagicMock
from utils.logger import log_result_and_type



class TestDecoratedLogger(unittest.TestCase):
    def test_log_result_and_type(self):
        # Create a mock logger
        logger_mock = MagicMock()
        # Apply the decorator to the function
        decorated_function = log_result_and_type(logger=logger_mock)(str.lower)

        # Call the decorated function
        result = decorated_function('ABCDE')

        # Assert that the result is correct
        self.assertEqual(result, 'abcde')

        # Assert that the logger was called with the correct message
        logger_mock.log_debug.assert_called_with("Result of lower: abcde (Type: str)")
    
if __name__ == '__main__':
    unittest.main()