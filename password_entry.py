"""
Timothy Yanner
"""

user_password = input("What is your password? ")

while len(user_password) < 5:
    user_password = input("What is your password? ")

print('*' * len(user_password))