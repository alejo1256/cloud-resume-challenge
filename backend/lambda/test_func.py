import unittest
from unittest.mock import MagicMock, patch
import json
import sys
import os

# Add the lambda directory to the path so we can import func
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import func

class TestLambda(unittest.TestCase):

    @patch('func.table')
    def test_lambda_handler(self, mock_table):
        # Mock the DynamoDB response
        mock_table.update_item.return_value = {
            'Attributes': {
                'visitor_count': 5
            }
        }
        
        # Call the lambda handler
        event = {}
        context = MagicMock()
        response = func.lambda_handler(event, context)
        
        # Verify the response
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['count'], 5)
        self.assertEqual(response['headers']['Access-Control-Allow-Origin'], '*')

if __name__ == '__main__':
    unittest.main()
