#d={"id":1,"krestni":"Jiri","prijmeni":"Cech"}

#print(d.get("krestni"))
#for to in d:
 	#print(to,d[to])
 	#print(d[to])
    #print(to)
    #print(d["prijmeni"])


# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+"."+last+ "@gmail.com"
#
#     def fullname(self):
#         print("{} {}".format(self.first,self.last))
#
#
#
# emp1=Employee("Jiri","Cech",10000)  #instance of the class Employee, instance variables are uniqe for each instance of the class-class variables are shared among all instances of the class.
# emp2=Employee("Paja","Xaverova",20000)
#
# print(emp1.email)
# print(emp2.email)
# print(emp2.fullname())
# print(Employee.fullname(emp1))

# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+"."+last+ "@gmail.com"
#
#     def fullname(self):
#         print("{} {}".format(self.first,self.last))
#
#     def apply_raise(self):
#         self.pay=int(self.pay * 1.04)
#
#
#
# emp1=Employee("Jiri","Cech",10000)
# emp2=Employee("Paja","Xaverova",20000)
#
# print(emp1.pay)
# emp1.apply_raise()
# print(emp2.pay)
# print(emp1.pay)

# class Employee:
#
#     num_of_empl=0
#     raise_amount =1.04 #class variable
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+"."+last+ "@gmail.com"
#
#         Employee.num_of_empl+=1  #init se provede vzdy
#
#     def fullname(self):
#         print("{} {}".format(self.first,self.last))
#
#     def apply_raise(self):
#         self.pay=int(self.pay * self.raise_amount) #give us the ability to change that amount for a single instance if we really wanted to.
#
#
# print(Employee.num_of_empl)  #pred inicialiizaci 0, po inicializaci 2 => emp1 a emp2
# emp1=Employee("Jiri","Cech",10000)
# emp2=Employee("Paja","Xaverova",20000)
#
# print(Employee.num_of_empl)
#
#
# #Employee.raise_amount=1.05
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
#
# emp1.raise_amount=1.06  #has raised amount within its namespace equal to 1.06 and it find that value before going and searching the class
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# class Employee:
#
#     num_of_empl=0
#     raise_amount =1.04 #class variable
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+"."+last+ "@gmail.com"
#
#         Employee.num_of_empl+=1  #init se provede vzdy
#
#     def fullname(self):
#         print("{} {}".format(self.first,self.last))
#
#     def apply_raise(self):
#         self.pay=int(self.pay * self.raise_amount) #give us the ability to change that amount for a single instance if we really wanted to.
#
#     @classmethod #class method decorator, instead of instance as first argument it enable to use class as the first argument. we can use these class methods as alternative constructors in order to provide mutiple ways of creating our objects.
#     def set_raise_amount(cls,amount): #cls je class variable name, jako je self u instance variable name.
#         cls.raise_amount=amount
#
#
# print(Employee.num_of_empl)  #pred inicialiizaci 0, po inicializaci 2 => emp1 a emp2
# emp1=Employee("Jiri","Cech",10000)
# emp2=Employee("Paja","Xaverova",20000)
#
# print(Employee.num_of_empl)
#
# emp1.raise_amount=1.07
# #Employee.raise_amount=1.05
# Employee.set_raise_amount(1.05) #class methot=> we are working with the class instead of the instance
# emp1.set_raise_amount(1.05) #we can run that class method from the instance
#
#
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# class Employee:
#
#     num_of_empl=0
#     raise_amount =1.04 #class variable
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+"."+last+ "@gmail.com"
#
#         Employee.num_of_empl+=1  #init se provede vzdy
#
#     def fullname(self):
#         print("{} {}".format(self.first,self.last))
#
#     def apply_raise(self):
#         self.pay=int(self.pay * self.raise_amount) #give us the ability to change that amount for a single instance if we really wanted to.
#
#     @classmethod #class method decorator, instead of instance as first argument it enable to use class as the first argument.
#     def set_raise_amount(cls,amount): #cls je class variable name, jako je self u instance variable name.
#         cls.raise_amount=amount
#
#     @classmethod #we can use these class methods as alternative constructors in order to provide mutiple ways of creating our objects.
#     def from_string(cls,emp_str):
#         first, last, pay = emp_str.split("-")
#         return cls(first,last,pay)
#
#     @staticmethod #staticmethod don't pass instance or class as the first argument, so they really behave just like rugular functions, but we include in our classes because they have some logical connection with the class.
#     def is_workday(day):  #Monday =0, Tue=1....Sunday=6.
#         if day.weekday()==5 or day.weekday()==6:
#             return False
#         return True
#
# import datetime
# mydate=datetime.date(2016,7,10)
# print(Employee.is_workday(mydate))
#
# print(Employee.num_of_empl)  #pred inicialiizaci 0, po inicializaci 2 => emp1 a emp2
# emp1=Employee("Jiri","Cech",10000)
# emp2=Employee("Paja","Xaverova",20000)
#
# print(Employee.num_of_empl)
#
# emp_str_1="John-Doe-7000"
# emp_str_2="Jane-Alex-8000"
# emp_str_3="Mil-Ad-3000"
#
# new_emp_1=Employee.from_string(emp_str_1)
# #first,last,pay=emp_str_1.split("-")
# #new_emp_1=Employee(first,last,pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)


class Employee:

    num_of_empl=0
    raise_amount =1.04 #class variable

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+ "@gmail.com"

        Employee.num_of_empl+=1  #init se provede vzdy

    def fullname(self):
        print("{} {}".format(self.first,self.last))

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount) #give us the ability to change that amount for a single instance if we really wanted to.

    @classmethod #class method decorator, instead of instance as first argument it enable to use class as the first argument.
    def set_raise_amount(cls,amount): #cls je class variable name, jako je self u instance variable name.
        cls.raise_amount=amount

    @classmethod #we can use these class methods as alternative constructors in order to provide mutiple ways of creating our objects.
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first,last,pay)

    @staticmethod #staticmethod don't pass instance or class as the first argument, so they really behave just like rugular functions, but we include in our classes because they have some logical connection with the class.
    def is_workday(day):  #Monday =0, Tue=1....Sunday=6.
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lan):
        super().__init__(first,last,pay)
        self.prog_lan=prog_lan

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None): #the list of employess set as default to None, because it can be mutable data=>dictionary or list....
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]  #set our employees to an empty list if the argument is not provided and set them equal to that employees list if it is.
        else:
            self.employees =employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())




dev1=Developer("Jiri","Cech",10000,"Python")
dev2=Developer("Paja","Xaverova",20000,"Java")

mgr1=Manager("Sue","Smith",30000,[dev1])
mgr1.add_emp(dev2)
#mgr1.remove_emp(dev1)
mgr1.print_emps()
print(mgr1.email)

print(isinstance(mgr1,Manager))  #built-in function to verify if mgr1 is instance of Manager.
print(isinstance(mgr1,Developer))
print(isinstance(mgr1,Employee))

print(issubclass(Manager,Employee)) #if the Manager class is the subclass of the Employee
print(issubclass(Manager,Developer))





#########################################################################################


u = "Jan Novák"
v = "Josef Nový"
print("u: {0} v: {1}".format(u, v))

