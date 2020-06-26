try:
    while True:
        name = str(int(float(input("Please enter the name: "))))
        if len(name)>=8:
            print("Name looks good")

        elif len(name)<8:
            print("Name should be at least 8 characters long")

        else:
            print("Please enter correct name")

except Exception as e:
    print("Invalid name")