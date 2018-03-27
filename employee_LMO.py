#Créer une classe employee
#Avec une méthode __init__ qui prend name et salary comme paramètres
#Créer une variable de classe globale, faire des recherches sur le net
#Créer une méthode displaycount qui affiche le nombre d'employés
#Créer une méthode display qui affiche un employé



class Employee:
    nEmployee = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.nEmployee += 1
    def __str__(self):
        return '[Employee[name : {}, salary : {} ]]'.format(self.name, self.salary)
    def display(self):
        print('nom : ', self.name, ', salaire : ', self.salary)
    def displaycount(self):
        print(Employee.nEmployee)


a = Employee('Toto', 200)
a.displaycount()
a.display()

b = Employee('Riri', 250)
b.displaycount()
b.display()

print(Employee.nEmployee)
