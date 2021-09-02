#!/usr/bin/env python3
"""
A simple application to store passwords
"""

# user class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


user1 = User("ismailpervez", "password123")
print(user1.username)