import re
e = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("enter your email: ")

if re.search(e, user_email):
    print("congratulation.....")
else:
    print("sorry, try agian")    