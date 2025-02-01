class Student:
    def __init__(self, height, gender, name, surname):
        self.height = height
        self.gender = gender
        self.name = name
        self.surname = surname

Ronaldo = Student(188, "SigmaMale", "Cristiano", "Ronaldo")
Leonel = Student(163, "loshara", "Leonel", "Messi")
print("Name: ", Leonel.name, "\nSurname: ", Leonel.surname, "\nGender: ", Leonel.gender, "\nHeight: ", Leonel.height)
print("\n")
print("Name: ", Ronaldo.name, "\nSurname: ", Ronaldo.surname, "\nGender: ", Ronaldo.gender, "\nHeight: ", Ronaldo.height)


'''DONT DO LIKE THAT!!!!!!!'''
Names = ["Messi", "Pessi", "ChupaChups"]
Surnames = ["Qurbanov", "Rahmanova", "Rahimli"]

Surnames.pop(0)

print("Surnames after deletion:", Surnames)
print("\n\nName:", Names[0], "\nSurname:", Surnames[0])
