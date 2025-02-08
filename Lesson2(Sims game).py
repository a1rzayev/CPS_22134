import random


class Job:
    def __init__ (self, name:str = "example_job", salary:float = 1):
        self.name = name
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




programmer = Job("Programmer", 1500)
Shamsaddin = Human("Shamsaddin", programmer, None, None, 0.25)

print(f"Job:\n\tName: {programmer.name}\n\tSalary: {programmer.salary}")

print(f"Human:\n\tName: {Shamsaddin.name}\n\tJob: {Shamsaddin.job.name} with salary {Shamsaddin.job.salary}\n\tHome: {Shamsaddin.home}\n\tCar: {Shamsaddin.car}\n\tMoney: {Shamsaddin.money}")
    


