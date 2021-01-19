# from pprint import pprint
import warnings
import unittest
import boto3
from moto import mock_dynamodb2
import sys
sys.path.insert(1, '../src/')


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<socket.socket.*>")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="callable is None.*")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="Using or importing.*")
        """Create the mock database and table"""
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.uuid = "123e4567-e89b-12d3-a456-426614174000"
        self.text = "Aprender DevOps y Cloud en la UNIR"

        from tests import ToDoCreateTable
        self.table = ToDoCreateTable.create_todo_table(self.dynamodb)
        self.table_local = ToDoCreateTable.create_todo_table()
        
        
    
    
    def tearDown(self):
        """Delete mock database and table after test is run"""
        self.table.delete()
        self.table_local.delete()

        self.dynamodb = None
        
        
    def test_table_exists(self):
        self.assertTrue(self.table)  # check if we got a result
        self.assertTrue(self.table_local)  # check if we got a result

        # check if the table name is 'ToDo'
        self.assertIn('todoTable', self.table.name)
        self.assertIn('todoTable', self.table_local.name)

        # pprint(self.table.name)    
if __name__ == '__main__':
    unittest.main()
