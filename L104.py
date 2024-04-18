#Emma and Abby
#Lab 10 part D

class Fabric:
    def __init__(self,countryoforigin, color):
        self.countryoforigin = countryoforigin
        self.color = color

    def __str__(self):
        return self.countryoforigin + "(" + str(self.color) + ")"

f1 = Fabric("France","chartreuse")
print(f1)


