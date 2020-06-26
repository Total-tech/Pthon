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



class player:
    no_of_games = 4
    def __init__(self,aname,fagame,ano_of_games):
        self.name = aname
        self.fgame = fagame
        self.no_of_games = ano_of_games

    def printabout(self):
        print(f"the name is {self.name} the favourate game is {self.fgame} and no of games are {self.no_of_games} ")



class CoolProggrammer(Employee,player):
    pass
shubham = player("Shubhu","cricket",4)
karan = player("Karan","Football",3)
raj = player("Raj","badminton",2)
# raj.printabout()
yovi = Employee("Totalmad_3.0",123456789,"Founder of ms")
kaavi = Employee("Agent S",12345,"Founder of linux")
jeeshanth=Employee("Jesh",1234,"Founder of mac")
rajat = CoolProggrammer("Rajat",12345,"Proggrammer")
det = rajat.printdetails()
print(det)