# Creer une classe Employee
# avec une methode __init__ qui prend name et salary comme parametres
# creer une variable de classe globale qui compte les employes, faire des recherches
# creer une methode displaycount qui affichele nombre d'employes
# creer une methode displayEmployee qui affiche un employe

class Employee():
    nbrEmployes = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.nbrEmployes += 1

    def displaycount(self):
        print("Total employee = {}".format(Employee.nbrEmployes))

    def displayEmployee(self):
        print("Name : {} salary : {}".format(Employee.name, Employee.salary))


emp01 = Employee("Spamus", 2000)
emp02 = Employee("Eggoz", 5000)
emp03 = Employee("Eggyspa", 7000)

emp01.displayEmployee()
emp02.displayEmployee()
emp03.displayEmployee()

emp03.displaycount()

print("Total employee = {}".format(Employee.nbrEmployes))
