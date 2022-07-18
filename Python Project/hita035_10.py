# Program to check validity of a password

# Importing the regular expression module
import re

# Initializing flag as zero
flag = 0

# Taking password as input from the user
pw = input("Enter the password: ")

#checking various conditions to check validity of the password, making flag = 1 if condition is not satisfied
if not re.search('[0-9]', pw):
    flag = 1

if not re.search('[a-z]', pw):
    flag = 1

if not re.search('[A-Z]', pw):
    flag = 1

if not re.search('[$.#,@]', pw):
    flag = 1

if len(pw) < 6 and len(pw) > 12:
    flag = 1

# Printing validity of password; valid if flag = 0
if (flag == 0):
    print('Password is valid')
else:
    print('Password is invalid')



