#!/usr/bin/env python3
"""
A simple application to store passwords
"""

class Credential:
    def __init__(self, accountName, password):
        self.accountName = accountName
        self.password = password

# user class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# user1 = User("ismailpervez", "password123")
# cred1 = Credential("twitter", "password001")
# print(user1.username)
# print(cred1.accountName)