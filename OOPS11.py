class Actor:
    def __init__(self,fname,lname,):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}_{lname}@gmail.com"

    @property
    def printemail(self):
        return f"{fname}_{lname}@gmail.com"

Sharukh = Actor("Sharukh","Khan")
Salmaan = Actor("Salmaan","Khan")
print(Sharukh.printemail())