# creer une classe employee
# avec une methode __init__ qui prend name et salary comme parameters
# creer une variable de classe globale qui compte les employees, faire des recherches google
# creer une methode displaycount qui affiche le nombre d'employees
# creer une methode display qui affiche un employee


class Employee(object):
    count = 0
    deleteCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
        Employee.deleteCount += 1

    def __del__(self):
        Employee.count -= 1

    def display(self):
        print(self.name + ' has got ' + self.salary)


def displayCount(Employee):
    print("Total employees are : {}".format(Employee.count))


a = Employee('jean', '30k')
b = Employee('dj', '100k')
c = Employee('jay', '1000k')


a.display()
b.display()
c.display()
displayCount(Employee)
del a
displayCount(Employee)
