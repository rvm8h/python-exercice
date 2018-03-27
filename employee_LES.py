# creer une classe employee
# avec une methode __init__ qui prend un name et salary comme parameters
# creer une variable de classe globale qui compte les employes , faire des recherches google
# creer une methode displaycount qui affiche le nombre d'employes
# creer une methode display qui affiche un employe

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.Name = name
        self.Salary = salary
        Employee.empCount += 1

    def displayEmployee(self):
        print("Nom :", self.Name, ", Salaire :", self.Salary)

    def displaycount(self):
        print("Total employees 2 =", Employee.empCount)


emp1 = Employee("Lorenzo", 35)
emp2 = Employee("Laurent", 30)
emp3 = Employee("Bob", 30)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

print("Total employees 1 = {}".format(Employee.empCount))

print(emp1.displaycount())
