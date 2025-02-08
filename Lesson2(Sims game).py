import random


class Job:
    def __init__ (self, name:str = "example_job", salary:float = 1):
        self.name = name
        self.salary = salary

#setters 
    #change name
    def set_name(self, name:str):
        self.name = name

    #change salary
    def set_salary(self, salary:float):
        self.salary = salary


class Human:
    #initialize person
    def __init__ (self, name:str, job:Job = None, home = None, car = None, money:float = 0):
        self.name = name
        self.job = job
        self.home = home
        self.happiness = 100
        self.satiety = 100
        self.car = car
        self.money = money

#setters
    #buy name
    def set_name(self, name): 
        self.name = name

    #buy home
    def set_home(self, home): 
        self.home = home

    #buy car
    def set_car(self, car): 
        self.car = car

    #buy job
    def set_job(self, job): 
        self.job = job

#funcs
    #eat
    def eat(self):
        self.satiety += 10
    
    #get salary 
    def work(self):
        self.money += self.job.salary



#link classes
programmer = Job("Programmer", 1500)
it_specialist = Job("It specialist", 1000)
deputat = Job("Dovlet qulluqcusu", 6000)
Shamsaddin = Human("Shamsaddin", deputat, None, None, 0.25)

print(f"Job:\n\tName: {programmer.name}\n\tSalary: {programmer.salary}")

print(f"Human:\n\tName: {Shamsaddin.name}\n\tJob: {Shamsaddin.job.name} with salary {Shamsaddin.job.salary}\n\tHome: {Shamsaddin.home}\n\tCar: {Shamsaddin.car}\n\tMoney: {Shamsaddin.money}")
    

#setters
simple_job = Job()
print(f"Job:\n\tName: {simple_job.name}\n\tSalary: {simple_job.salary}")

new_name = input("Input new job name: ")
new_salary = float(input("Input new job salary: "))

simple_job.set_salary(new_salary)
simple_job.set_name(new_name)

print(f"Job:\n\tName: {simple_job.name}\n\tSalary: {simple_job.salary}")
