#!/usr/bin/env python3
import unittest
from unittest import result
import main

class TestMain(unittest.TestCase):
    
    def test_User(self):
        user1 = main.User("ismailpervez", "pass123")
        result = user1.username
        """
        testing get_creds() method
        """
        result2 = user1.get_creds(user1.password)

        """
        testing store_password() method
        """
        test_cred = main.Credential("insta", "pass123")
        result3 = user1.store_password(test_cred)

        self.assertEqual(result, "ismailpervez")
        self.assertEqual(result2, "no password saved yet")
        self.assertEqual(result3, "cred stored successfully!")

    def test_Credential(self):
        """
        test for Credential class
        """
        cred1 = main.Credential("twitter", "twitter_password")
        result = cred1.account_name

        self.assertEqual(result, "twitter")


if __name__ == "__main__":
    unittest.main()