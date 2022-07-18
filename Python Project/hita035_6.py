# Program to find sum and product of complex numbers using magic methods

# Importing the math module
import math

# Creating a class complex to add and multiply two complex numbers
class Complex:

# Initializing the real and imaginary values in __init__ function
    def __init__(self,a):
        self.real = float(input(f'Enter the real value of complex number {a}: '))
        self.img = float(input(f'Enter the imaginary value complex number {a}: '))

# Creating a function to find the absolute value of the complex number
    def absolute(self):
        abs = float(math.sqrt(self.real ** 2 + self.img ** 2))
        print(f"Absolute value= {abs:.4f}")

# Function to add two complex numbers
    def __add__(self, A):
        return complex(A.real + self.real, A.img + self.img)

# Function to multiply two complex numbers
    def __mul__(self, A):
        return complex(A.real * self.real - A.img * self.img, A.real
                       * self.img + A.img * self.real)

# Main function to call various functions in the class
def main():

# Object for 1st complex number
    c1 = Complex(1)
    Complex.absolute(c1)

# Object for 2nd complex number
    c2 = Complex(2)
    Complex.absolute(c2)

# Adding two complex numbers using magic method
    c3 = c1+c2

# Multiplying two complex numbers using magic method
    c4 = c1*c2
    print (f'Sum of the of complex numbers = {c3}')
    print (f'Product of the complex numbers = {c4}')

# Calling the main function
if __name__ == '__main__':
    main()




