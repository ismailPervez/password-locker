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

        self.assertEqual(result, "ismailpervez")
        self.assertEqual(result2, "no password saved yet")

    def test_Credential(self):
        cred1 = main.Credential("twitter", "twitter_password")
        result = cred1.account_name

        self.assertEqual(result, "twitter")


if __name__ == "__main__":
    unittest.main()