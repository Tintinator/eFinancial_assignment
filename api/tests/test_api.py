from mock_db import MockDB
from mock import patch
import api


class TestUtils(MockDB):
    def test_db_write(self):
        with self.mock_db_config:
            self.assertEqual(api.create_entry(), True)

