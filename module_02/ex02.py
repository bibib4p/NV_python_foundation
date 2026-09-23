# password gate
username_input = input("Username: ")
password_input = input("Password: ")

username = "kyarphyu"
password = "@3nI98_"

if username_input == username and password_input == password:
    print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")

# Would this be a secure way to build a real authentication system? Why or why not?
# No because it is stored as plain text with no encryption.