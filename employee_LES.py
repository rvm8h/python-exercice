# creer une classe employee
# avec une methode __init__ qui prend un name et salary comme parameters
# creer une variable de classe globale qui compte les employes , faire des recherches google
# creer une methode displaycount qui affiche le nombre d'employes
# creer une methode display qui affiche un employe

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayEmployee(self):
        print("Nom :", self.name, ", Salaire :", self.salary)

    def displaycount(self):
        txt = "Total employees par displaycount = {}"
        return txt.format(self.empCount)

emp1 = Employee("Lorenzo", 35)
emp2 = Employee("Laurent", 30)
emp3 = Employee("Bob", 30)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

print("Total employees = {}".format(Employee.empCount))

print(emp1.displaycount())
