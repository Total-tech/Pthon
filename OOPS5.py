class Employee:
    no_of_leaves = 8




    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole




    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print(f"{string} is good")

class programmer(Employee):
    no_of_holidays = 87

    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

    def printprog(self):
        return f"the programmer's name is {self.name} ,salary is {self.salary}, role is {self.role} and he knows {self.languages} language"




yovi = Employee("Totalmad_3.0",123456789,"Founder of ms")
kaavi = Employee("Agent S",12345,"Founder of linux")
jeeshanth=Employee("Jesh",1234,"Founder of mac")

shubham = programmer("Shubhu",12345,"Employee of ms","python")
carry = programmer("Carry",12345,"Employee of linux","JavaScript")
karan = programmer("karan",12345,"Employee of mac","C++")
print(shubham.printprog())