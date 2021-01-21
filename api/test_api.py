import json
import unittest
import api
from mock import patch
from mock_db import MockDB


class TestApi(MockDB):
    def test_entry(self):
        pass

    def test_create_entry(self):
        pass

    def test_read_entry(self):
        pass

    def test_update_entry(self):
        pass

    def test_delete_entry(self):
        pass

    def test_db_read(self):
        pass

    def test_db_write(self):
        # Entry Creation
        self.assertEqual(
            api.db_write(
                """INSERT INTO `tbl_entry` (`entry_title`, `entry_date`, `entry_content`) VALUES
                            ('Test Title', '2021-01-21', 'Hi This is a test')"""
            ),
            True,
        )
        self.assertEqual(
            api.db_write(
                """INSERT INTO `tbl_entry` (`title`, `entry_date`, `entry_content`) VALUES
                            ('Test Title', '2021-01-21', 'Hi This is a test')"""
            ),
            False,
        )
        self.assertEqual(
            api.db_write(
                """INSERT INTO `tbl_entry` (`entry_title`, `entry_date`, `entry_content`) VALUES
                            ('Test Title', 'asdf', 'Hi This is a test')"""
            ),
            False,
        )
        # Entry Update
        self.assertEqual(
            api.db_write(
                """UPDATE `tbl_entry` SET entry_title='Updated Title' WHERE entry_id='1' """
            ),
            True,
        )
        self.assertEqual(
            api.db_write(
                """UPDATE `tbl_entry` SET entry_title='Updated Title' WHERE entry_id='30' """
            ),
            True,
        )
        self.assertEqual(
            api.db_write(
                """UPDATE `tbl_entry` SET title='Updated Title' WHERE entry_id='1' """
            ),
            False,
        )
        # Entry Deletion
        self.assertEqual(
            api.db_write(
                """UPDATE `tbl_entry` SET title='Updated Title' WHERE entry_id='1' """
            ),
            True,
        )
        pass

    def test_createResponse(self):
        pass


if __name__ == "__main__":
    unittest.main()
