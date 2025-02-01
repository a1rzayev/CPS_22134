class Student:
    def __init__(self, height, gender, name, surname):
        self.height = height
        self.gender = gender
        self.name = name
        self.surname = surname
    def go_to_school(self, schoolname):
        print(f"I go to {schoolname} school")
        

Hikmet = Student(153, "male", "Hikmet", "Qurbanov")
print("Name: ", Hikmet.name, "\nSurname: ", Hikmet.surname, "\nGender: ", Hikmet.gender, "\nHeight: ", Hikmet.height)
Hikmet.go_to_school("IB")
print("\n")


Medina = Student(163, "female", "Medina", "Rahmanova")
print("Name: ", Medina.name, "\nSurname: ", Medina.surname, "\nGender: ", Medina.gender, "\nHeight: ", Medina.height)
Medina.go_to_school("ABC")

'''DONT DO LIKE THAT!!!!!!!'''
# Names = ["Hikmet", "Medina", "Aziz"]
# Surnames = ["Qurbanov", "Rahmanova", "Rahimli"]

# Surnames.pop(0)

# print("Surnames after deletion:", Surnames)
# print("\n\nName:", Names[0], "\nSurname:", Surnames[0])