class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.arole = arole
    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}"


# yovi = Employee()
# KAAVI = Employee()
# yovi.name = "Totalmad_3.0"
# yovi.role = "Founder of microsoft"
# yovi.salary = "$987654321999"
# KAAVI.name = "Agent s"
# KAAVI.role = "Founder of linux"
# KAAVI.salary = "$123321432"
yovi = Employee("Totalmad_3.0",123456789,"Founder of ms")
print(yovi.salary)