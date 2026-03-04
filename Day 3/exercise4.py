# Set the password
PASSWORD = "s3cur3P@ss"

# Prompt the user until they enter the correct password
while True:
    user_input = input("Enter the password: ")
    if user_input == PASSWORD:
        print("Access Granted!")
        break
    else:
        print("Incorrect password. Try again.")