import unittest
from unittest.mock import patch
import pandas as pd
from main import average_sugars_by_calorie_range

class TestAverageSugarsByCalorieRange(unittest.TestCase):

    @patch("main.pd.read_csv")
    def test_average_sugars_by_calorie_range(self, mock_read_csv):
        mock_data = pd.DataFrame({
            "calories": [45, 80, 110, 150, 200, 320, 330],
            "sugars": [5, 6, 7, 8, 9, 10, 11],
        })
        mock_read_csv.return_value = mock_data

        result = average_sugars_by_calorie_range(mock_data)
        
        expected_result = {
            "0-50 calories": 5.0,
            "50-100 calories": 6.0,
            "100-150 calories": 7.5,
            "150-200 calories": 9.0,
            "Over 300 calories": 10.5,
        }

        for key in expected_result:
            self.assertAlmostEqual(result.get(key), expected_result[key], places=2)

    def test_empty_data(self):
        empty_data = pd.DataFrame(columns=["calories", "sugars"])
        result = average_sugars_by_calorie_range(empty_data)
        
        expected_result = {
            "0-50 calories": 0.0,
            "50-100 calories": 0.0,
            "100-150 calories": 0.0,
            "150-200 calories": 0.0,
            "Over 300 calories": 0.0,
        }
        
        self.assertEqual(result, expected_result)

    def test_no_sugars_in_some_ranges(self):
        partial_data = pd.DataFrame({
            "calories": [45, 320],
            "sugars": [5, 10]
        })
        result = average_sugars_by_calorie_range(partial_data)
        
        expected_result = {
            "0-50 calories": 5.0,
            "50-100 calories": 0.0,
            "100-150 calories": 0.0,
            "150-200 calories": 0.0,
            "Over 300 calories": 10.0,
        }

        for key in expected_result:
            self.assertAlmostEqual(result.get(key), expected_result[key], places=2)

if __name__ == "__main__":
    unittest.main()
