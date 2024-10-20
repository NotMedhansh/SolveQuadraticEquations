import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return root1, root2

def main():
    print("Quadratic Equation Solver")
    
    # Input coefficients
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a == 0:
        print("Coefficient 'a' cannot be zero in a quadratic equation.")
        return
    
    # Solve the quadratic equation
    root1, root2 = solve_quadratic(a, b, c)
    
    # Output the roots
    print(f"The roots are: {root1} and {root2}")

if __name__ == "__main__":
    main()
