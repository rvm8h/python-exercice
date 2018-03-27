# creer une classe employee
# avec une methode __init__ qui prend  nmae et salary comme parameters
# creer une variable de classe globale qui compte les employes , faire des recherches google
# creer une methode displaycount qui affiche le nombre d'employes
# creer une methode display qui affiche un employe


class Employee:
#'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee {}".format(Employee.empCount))
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)




emp1 = Employee("Zara", 2000)
emp2 = Employee("Bob",5000)
emp3 = Employee('Thomas',7000)


emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp3.displayCount()
print("Total Employee={}".format(Employee.empCount))


