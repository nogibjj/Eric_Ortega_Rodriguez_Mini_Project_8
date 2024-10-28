import unittest
from unittest.mock import patch
import pandas as pd
from main import average_sugars_by_calorie_range

class TestAverageSugarsByCalorieRange(unittest.TestCase):

    @patch('main.pd.read_csv')
    def test_average_sugars_by_calorie_range(self, mock_read_csv):
        # Create a mock dataset that covers all necessary calorie ranges
        mock_data = pd.DataFrame({
            'calories': [45, 80, 110, 150, 200, 320, 330],
            'sugars': [5, 6, 7, 9, 8, 10, 11]
        })
        mock_read_csv.return_value = mock_data
        
        # Call the function and get the result
        result = average_sugars_by_calorie_range()

        # Expected values based on the filtered logic:
        expected_result = {
            '0-50 calories': 5.0,        # Only 45
            '50-100 calories': 6.0,      # Only 80
            '100-150 calories': 8.0,     # Only 150 (110 is included in this range if filtered correctly)
            '150-200 calories': 8.0,     # Only 200
            'Over 300 calories': 10.5    # Average of 10 and 11 (320, 330)
        }
        
        # Assert that result matches expected_result
        for key in expected_result:
            self.assertAlmostEqual(result.get(key), expected_result[key], places=2)

if __name__ == "__main__":
    unittest.main()
