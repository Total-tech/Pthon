try:
    while True:
        x = int(input("number: "))
        unit = (input("Lbs or Kg: "))
        if unit.lower()=="lbs":
            convert = x / 2.205
            print(convert)
        elif unit.lower()=="Kg":
            convert = x * 2.205
            print(convert)
except Exception as e:
    print(e)