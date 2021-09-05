#!/usr/bin/env python3
"""
A simple application to store passwords
"""

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

    def store_password(self, cred):
        #print(cred.account_name, cred.account_password)
        if isinstance(cred, Credential):
            if cred.account_name and cred.account_password:
                self.users_credentials.append(cred)
                print("cred stored successfully!")
                
            else:
                print("please provide an account name and password")
            
        else:
            print("please provide an account name and password")

class Credential:
    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

        if not self.account_password:
            # generate password
            random_password = ''.join(random.choices(string.ascii_letters, k=5)) + str(random.randint(0,10000))
            self.account_password = random_password

"""
starting point of main application functionality - creating an user account
"""
print("PASSWORD LOCKER")
new_username = input("enter your username: ")
new_passsword = input("enter your password: ")