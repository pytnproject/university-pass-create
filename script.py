print("Welcome! Follow the instructions to log in to the system.")

while True:
    stud_num = input("Enter your student number: ")
    length = len(stud_num)
    if length == 14:
        try:
            stud_num = int(stud_num)
            break
        except ValueError:
            print("The number you entered is not a number!") 
    else:
        print("The number is too short, it must consist of 14 digits.")   

stud_num = str(stud_num)        
stud_pass = stud_num[-4:] + "@AHUCM"

while True:
    password = input("Please enter your password (Hint: last 4 digits of your student number + @AHUCM): ")
    if password != stud_pass:
        print("Wrong password!")
    else:
        print("Access granted!")
        break    