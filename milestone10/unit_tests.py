import unittest
from unittest.mock import patch
from server import app


class TestWebServer(unittest.TestCase):

    def test_successful_birthdays_report(self):
        with app.test_client() as client:
            response = client.get('/birthdays?month=april&department=HR')
            self.assertEqual(response.status_code, 200)
 
           
    def test_successful_anniversaries_report(self):
        with app.test_client() as client:
            response = client.get('/anniversaries?month=april&department=Sales')
            self.assertEqual(response.status_code, 200)
      

    def test_missing_month_param_birthdays_report(self):
        with app.test_client() as client:
            response = client.get('birthdays?department=HR')
            self.assertEqual(response.status_code, 400)


    def test_missing_department_param_birthdays_report(self):
        with app.test_client() as client:
            response = client.get('/birthdays?month=april')
            self.assertEqual(response.status_code, 400)


    def test_missing_month_param_anniversaries_report(self):
        with app.test_client() as client:
            response = client.get('/anniversaries?department=Sales')
            self.assertEqual(response.status_code, 400)


    def test_missing_department_param_anniversaries_report(self):
        with app.test_client() as client:
            response = client.get('/anniversaries?month=april')
            self.assertEqual(response.status_code, 400)


    @patch('report.load_employees')
    def test_corrupted_csv_file(self, mock_load_employees):
        mock_load_employees.side_effect  = Exception('Cant load data')     
        with app.test_client() as client:
            response = client.get('/anniversaries?month=april&department=HR')
            self.assertEqual(response.status_code, 500)
            

if __name__ == '__main__':
    unittest.main()
