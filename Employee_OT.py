# creer une classe employee
# avec une methode __init__ qui prend un name et salary comme parameters
# creer une variable de classe globale qui compte les employes , faire des recherches google
# creer une methode displaycount qui affiche le nombre d'employes
# creer une methode display qui affiche un employe



class employee():

    CountEmployee = 0

    def __init__(self, name, salary):
        self.DataName = name
        self.DataSalary = salary
        employee.CountEmployee += 1

    def displaycount(self):
        print("Number of employee(s): {}".format(self.CountEmployee))

    def displayemployee(self):
        print("Employee: {}, salary: {}".format(self.DataName,self.DataSalary))


x = employee("Leon", 40000)
y = employee("Florence", 45000)
z = employee("Bob", 35000)

z.displaycount()
y.displayemployee()
