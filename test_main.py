#!/usr/bin/env python3
import unittest
from unittest import result
import main

class TestMain(unittest.TestCase):
    
    def test_User(self):
        user1 = main.User("ismailpervez", "pass123")
        result = user1.username
        result2 = user1.get_creds(user1.password)

        self.assertEqual(result, "ismailpervez")
        self.assertEqual(result2, [])

if __name__ == "__main__":
    unittest.main()