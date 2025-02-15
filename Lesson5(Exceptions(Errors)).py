#try и except обязательные! 
try:
    age = int(input("Input number: "))
except ValueError:
    print("value error!")
#else и finally необязательные
else:
    print("other")
finally: 
    print("code is not stopped")
