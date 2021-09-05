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
a user also has a list containing saved
"""
class User:
    users_credentials = []
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_creds(self, user_input_password):
        if (user_input_password == self.password):
            #print(self.users_credentials)
            if len(self.users_credentials) == 0:
                print("no password saved yet")

            for cred in self.users_credentials:
                print(f"password for {cred.account_name} account is {cred.account_password}")

        else:
            print("wrong password!")

