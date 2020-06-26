a = input("what is your name: ")

if a.isnumeric():
    raise Exception("num not allowed")

else:
    print(f"hello {a}")