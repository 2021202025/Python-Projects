while True:
    password = input("Enter the password: ")
    if (any(char.isdigit() for char in password)):
        if(len(password) >= 5):
            if(any(char.isupper() for char in password)):
                print("Success")
                break
            else:
                print("Must contain at least 1 Upper Case")
        else:
            print("Must over 5 chars in length")
    else:
        print("Must contain a number")

print(password)


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)