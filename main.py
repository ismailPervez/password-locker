#!/usr/bin/env python3
"""
A simple application to store passwords
"""

class Credential:
    def __init__(self, accountName, password):
        self.accountName = accountName
        self.password = password
"""
class User is used as a blueprint for a user
a user is required to have a username and a password to access his/her credentials
a user also has a list containing saved credentials
"""
class User:
    users_credentials = []
    def __init__(self, username, password):
        self.username = username
        self.password = password



