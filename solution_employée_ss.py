# creer une classe emloyee
# avec une methode _init qui prend name esalary comme parameters
#creer une varaiable de classe globle qui cmpte les employees faire des recherches
# creer une methode displaycount qui affiche le nombre demployés
# creer une methode display qui affiche un employe

class Employe():
    a = 0
    def __init__(self, name, salary):
         self.name = name
         self.salary = salary
         Employe.a += 1
    def displaycount(self):
      print("total Employés {}".format(Employe.a))
    def display(self):
         print("Name : ", self.name,"Salary", self.salary)


emp1 = Employe("zara", 2000)

emp1.displaycount()
emp1.display()