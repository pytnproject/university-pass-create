# Quick Start

Basic usage:

```bash
python script.py
```

<details>
<summary>Click to see full source code</summary>

```python
print("Welcome! Follow the instructions to log in to the system.")

while True:
    stud_num = input("Enter your student number: ")
    length = len(stud_num)
    if length == 14 and stud_num.isdigit():
        break
    else:
        print("The number is too short, it must consist of 14 digits.")

stud_pass = stud_num[-4:] + "@AHUCM"

while True:
    password = input("Please enter your password (Hint: last 4 digits of your student number + @AHUCM): ")
    if password != stud_pass:
        print("Wrong password!")
    else:
        print("Access granted!")
        break
```

</details>

<details>
<summary>Click to see example session</summary>

```
Welcome! Follow the instructions to log in to the system.
Enter your student number: 12345678901234
Please enter your password (Hint: last 4 digits of your student number + @AHUCM): 1234@AHUCM
Access granted!
```

</details>
