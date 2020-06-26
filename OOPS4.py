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


yovi = Employee.from_str("Totalmad_3.0-123456789-Founder of ms")
kaavi = Employee("Agent S",12345,"Founder of linux")
jeeshanth=Employee("Jesh",1234,"Founder of mac")
yovi.printgood("Yovi")