import unittest
from unittest.mock import patch
import pandas as pd
from main import average_sugars_by_calorie_range

class TestAverageSugarsByCalorieRange(unittest.TestCase):

    @patch('main.pd.read_csv')
    def test_average_sugars_by_calorie_range(self, mock_read_csv):
        # Create a mock dataset
        mock_data = pd.DataFrame({
            'calories': [45, 80, 110, 150, 200, 320, 330],
            'sugars': [5, 6, 7, 8, 9, 10, 11]
        })
        mock_read_csv.return_value = mock_data
        
        # Call the function and get the result
        result = average_sugars_by_calorie_range("/Users/ericortega/Eric_Ortega_Rodriguez_Mini_Project_8/data/cereal.csv")

        # Expected values based on the mock_data calorie and sugar columns
        expected_result = {
            '0-50 calories': 5.0,         # Only the 45 calorie item
            '50-100 calories': 6.0,       # Only the 80 calorie item
            '100-150 calories': 7.5,      # Average of 110 and 150 calorie items
            '150-200 calories': 9.0,      # Only the 200 calorie item
            'Over 300 calories': 10.5     # Average of 320 and 330 calorie items
        }
        
        # Assert that result matches expected_result
        for key in expected_result:
            self.assertAlmostEqual(result.get(key), expected_result[key], places=2)

if __name__ == "__main__":
    unittest.main()





# import unittest
# from unittest.mock import patch
# import pandas as pd
# from main import average_sugars_by_calorie_range

# class TestAverageSugarsByCalorieRange(unittest.TestCase):

#     def test_average_sugars_by_calorie_range(self):
#         # Create a mock dataset
#         mock_data = pd.DataFrame({
#             'calories': [45, 80, 110, 150, 200, 320, 330],
#             'sugars': [5, 6, 7, 8, 9, 10, 11]
#         })
        
#         # Use `patch` as a context manager to mock `pd.read_csv`
#         with patch('main.pd.read_csv', return_value=mock_data):
#             # Call the function and get the result
#             result = average_sugars_by_calorie_range()

#             # Expected values based on the mock_data calorie and sugar columns
#             expected_result = {
#                 '0-50 calories': 5.0,         # Only the 45 calorie item
#                 '50-100 calories': 6.0,       # Only the 80 calorie item
#                 '100-150 calories': 7.5,      # Average of 110 and 150 calorie items
#                 '150-200 calories': 9.0,      # Only the 200 calorie item
#                 'Over 300 calories': 10.5     # Average of 320 and 330 calorie items
#             }

#             # Assert that result matches expected_result
#             for key in expected_result:
#                 self.assertAlmostEqual(result.get(key), expected_result[key], places=2)

# if __name__ == "__main__":
#     unittest.main()
