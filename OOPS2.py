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
yovi = Employee("Totalmad_3.0",123456789,"Founder of ms")
kaavi = Employee("Agent S",12345,"Founder of linux")
yovi.change_leaves(44)
print(yovi.no_of_leaves)