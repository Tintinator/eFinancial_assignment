import mysql.connector
from mysql.connector import errorcode
from unittest import TestCase
from mock import patch
from flask_app import app
from config_data import test_user, test_password, test_port, test_host, test_db


class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        cnx = mysql.connector.connect(
            host=test_host, user=test_user, password=test_password, port=test_port
        )
        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute("DROP DATABASE {}".format(test_db))
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(test_db, err))

        # create database
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(test_db)
            )
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = test_db

        query = """CREATE TABLE `test_tbl_entry` (
                    `entry_id` int NOT NULL AUTO_INCREMENT,
                    `entry_title` varchar(50) NOT NULL,
                    `entry_date` date NOT NULL, 
                    `entry_content` varchar(500) NOT NULL,
                    PRIMARY KEY (`entry_id`)
                )"""
        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)

        cursor.close()
        cnx.close()

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=test_host, user=test_user, password=test_password
        )

        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute("DROP DATABASE {}".format(test_db))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(test_db))
        cnx.close()
