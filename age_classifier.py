running_status = True
while running_status:
    age = input("Enter your age:")
    if age.isdigit():
        age = int(age)
        if age == 1000:
            running_status = False
        elif age <= 0:         
            print("Invalid Age. Please enter an age greater than zero")
        elif age < 13:
            print("You are a child")
        elif age <= 19:
            print("You are a teenager")
        elif age < 60:
            print("You are an adult")
        else:
            print("You are a senior citizen")
    else:
        print("Invalid input.Please enter an integer")
