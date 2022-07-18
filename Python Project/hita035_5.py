# To find roots of a quadratic equations

#Creating a class quadratic for finding roots of a quadratic equation
class Quadratic:

# Initializing the three coefficients in __init__
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

# Creating a roots function to calculate the roots
    def roots(self):

# When the equation ia a linear equation
        if not self.a:
            root = int(-self.c / self.b)
        else:

# Finding the determinant d
            d = pow(self.b, 2) - 4 * self.a * self.c

# When d = 0; roots are real and equal
            if not d:
                root = (-self.b / (2 * self.a))
                print(f"Roots are real and equal and is : {root}")

# When d>0; roots are real and distinct
            elif d > 0:
                root1 = int((-self.b + pow(d, 0.5)) / (2 * self.a))
                root2 = int((-self.b - pow(d, 0.5)) / (2 * self.a))
                print(f"Roots are real and distinct = {root1} and {root2}")

# When d<0; roots are imaginary
            else:
                rp = int(-self.b / (2 * self.a))
                ip = int(pow(abs(d), 0.5) / (2 * self.a))
                print(f"Roots are imaginary and is = {rp}+{ip}i and {rp}-{ip}i")

# Main function to call the various functions in the class
def main():

# Data attributes for 1st object
    a, b, c = map(int, input("Enter a, b and c values: ").split())
    q = Quadratic(a,b,c)
    q.roots()

# Data attributes for 2nd object
    a, b, c = map(int, input("Enter a, b and c values: ").split())
    r = Quadratic(a, b, c)
    r.roots()

# Data attributes for 3rd object
    a, b, c = map(int, input("Enter a, b and c values: ").split())
    s = Quadratic(a, b, c)
    s.roots()

# To call the main function
if __name__ == "_main_":
    main()



