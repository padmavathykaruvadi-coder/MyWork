correct_password = "openAI123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_password = input("Enter password: ")
    attempts += 1   

    if entered_password == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")