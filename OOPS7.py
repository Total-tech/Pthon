class Grandpa:
    basketball = 1

class Dad(Grandpa):
    dance = 1
    def isdance(self):
        return f"yes i dance {self.dance} no of times"

class Son(Dad):
    dance = 6
    def isdance(self):
           return f"Yes ki dance awesomely {self.dance} no of times"

yovi = Grandpa()
jeeshanth = Dad()
shubham = Son()

print(shubham.isdance())