'''
Single inheritance
'''
# Single inheritance occurs when child class
# inherits only a single parent class.
# Base -> Derived
class employess:
    company = "google"

    def showdetail(self):
        print("this is an employee")
class programmer(employess):
    languages = "python"
    #company = "youtube  "

    def getlanguage(self):
        print(f"the language is {self.languages}")
    def showdetail(self):
        print("this is an programmer")
e = employess()
e.showdetail()
p = programmer()
p.showdetail()
print(p.company)
