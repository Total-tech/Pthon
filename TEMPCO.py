try:
    while True:
        x = int(input("number: "))
        unit = (input("Cf or Ck or Fc or Fk or Kc or Kf: "))
        if unit.lower()=="cf":
            convert = (x * 9/5) + 32
            print(convert)
        elif unit.lower()=="ck":
            convert = x + 273.15
            print(convert)
        elif unit.lower()=="fc":
            convert = (x - 32) * 5/9
            print(convert)
        elif unit.lower()=="fk":
            convert = (x - 32) * 5/9 + 273.15
            print(convert)
        elif unit.lower()=="kc":
            convert = 0 - 273.15
            print(convert)
        elif unit.lower()=="kf":
            convert = (99 - 273.15) * 9/5 + 32
            print(convert)
except Exception as e:
    print(e)