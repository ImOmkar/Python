class Employee:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
        
    def display(self):
        print('E_id: ',self.id)
        print('E_name: ',self.name)
        print('E_age: ',self.age)
        print('Post: ',self.desig)

    def __add__(self, a):
        maximum = self.salary
        for max in range(len(a)):
            if maximum <= a[max].salary:
                maximum = a[max].salary
                n=max

        print("Highest salary from the Managers: ")
        print("E_id: ",a[n].id)
        print("E_name: ",a[n].name)
        print("E_age: ",a[n].age)
        print("E_salary: ",a[n].salary)

    def __mul__(self, a):
        
        minimum = self.salary
        for min in range(len(a)):
            if minimum >= a[min].salary:
                minimum = a[min].salary
                p=min

        print("Lowest salary from the SW_developers: ")
        print("id: ",a[p].id)
        print("name: ",a[p].name)
        print("age: ",a[p].age)
        print("salary: ",a[p].salary)
      
class Manager(Employee):
    
    def __init__(self,m1,m2,m3,salary):
    
        self.desig="----Manager---"
        self.salary=salary

        Employee.__init__(self,m1,m2,m3)

class SoftDev(Employee):

    def __init__(self, sd1,sd2,sd3,salary):
        
        self.desig="---software developer---"
        self.salary=salary
        Employee.__init__(self,sd1,sd2,sd3)
        
a=[]
dev=[]

print("--Enter manager details--")
for i in range(5):
    
    m1=int(input("Enter Employee Id: "))
    m2=input("Enter Employee Name: ")
    m3=int(input("Enter Age: "))
    salary=float(input("Enter Salary: "))
    a.append(Manager(m1,m2,m3,salary))

print("--Enter SW.Developers details--")
for i in range(5):
           sd1=input("Enter Employee Id: ")
           sd2=input("Enter Employee Name: ")
           sd3=int(input("Enter Age: "))
           salary=float(input("Enter Salary: "))
           dev.append(SoftDev(sd1,sd2,sd3,salary))

for i in range(len(a)):
    a[i].display()
for i in range(len(a)):
    dev[i].display()

#operator overloading
a[0] + (a)
dev[0] * (dev)
print(Employee.__doc__)
