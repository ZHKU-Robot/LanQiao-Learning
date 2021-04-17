class Complex(object):
    def __init__(self, real=0, imagine=0):
        self.real = real
        self.imagine = imagine

    def __str__(self):
        return f"{self.real}+{self.imagine}i"
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imagine*other.imagine,self.real*other.imagine+other.real*self.imagine)

def getComplexNPower(n):
    complex1,complex2=Complex(2,3),Complex(2,3)
    complex3=complex1*complex2
    for i in range(n):
        complex3=complex3*Complex(2,3)
    print(complex3)
getComplexNPower(123455)
