import unittest
from unittest.mock import patch
import pandas as pd
import main 

class TestAverageSugarsByCalorieRange(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_average_sugars_by_calorie_range(self, mock_read_csv):
        # Create a DataFrame directly
        mock_df = pd.DataFrame({
            'calories': [50, 100, 150, 200, 250, 300, 350],
            'sugars': [6, 8, 5, 10, 4, 12, 9]
        })
        
        # Set the return value of read_csv to be this DataFrame
        mock_read_csv.return_value = mock_df

        # Capture the print output
        with patch("builtins.print") as mock_print:
            main.average_sugars_by_calorie_range()
            
            # Define the expected print output calls
            expected_calls = [
                ("Average sugars for cereals with 0-50 calories: 6.00",),
                ("Average sugars for cereals with 50-100 calories: 8.00",),
                ("Average sugars for cereals with 100-150 calories: 5.00",),
                ("Average sugars for cereals with 150-200 calories: 10.00",),
                ("Average sugars for cereals with 200-250 calories: 4.00",),
                ("Average sugars for cereals with 250-300 calories: 12.00",),
                ("Average sugars for cereals with Over 300 calories: 9.00",)
            ]
            mock_print.assert_has_calls([unittest.mock.call(*call) for call in expected_calls], any_order=False)

if __name__ == "__main__":
    unittest.main()
