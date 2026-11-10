# Login System Script

A simple Python login system that generates a password from the user's student number.

# Usage

```bash
python script.py
```

---

# Code 


```python
print("Welcome! Follow the instructions to log in to the system.")

attempts = 4

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

while attempts != 0:
    password = input("Please enter your password (Hint: last 4 digits of your student number + @AHUCM): ")
    if password != stud_pass:
        attempts = attempts - 1
        print(f"Wrong password! Attempts left: {attempts}")
        if attempts == 0:
            print("Access denied!")
    else:
        print("Access granted!")
        break
```

<details>
<summary>Example session</summary>

```
Welcome! Follow the instructions to log in to the system.
Enter your student number: 12345678901234
Please enter your password (Hint: last 4 digits of your student number + @AHUCM): 1234@AHUCM
Access granted!
```

</details>