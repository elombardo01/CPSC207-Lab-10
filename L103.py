#Emma and Abby
#Lab 10 part C

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "(" + str(self.age) + ")"

p1 = Person("John",36)

print(p1)

#This gives us John(36), which is the same as our guess.
