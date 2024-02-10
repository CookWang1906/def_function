#info: A basic math game using choice to choose function.
def pick():
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choices = int(input("Please choose a number to continue: "))

    if choices == 1:
        addition()
    elif choices == 2:
        subtraction()
    elif choices == 3:
     multiplication()
    elif choices == 4:
        division()
    else:
        print("Run again lil buddy.")
        return pick()

#choices
def addition():
    n1 = int(input("Enter your first number here: "))
    n2 = int(input("Enter your second number here: "))
    ans = n1 + n2
    print(f"{n1} + {n2} =", ans)
    return pick()
    
def subtraction():
    n1 = int(input("Enter your first number here: "))
    n2 = int(input("Enter your second number here: "))
    ans = n1 - n2
    print(f"{n1} - {n2} =", ans)
    return pick()
    
def multiplication():
    n1 = int(input("Enter your first number here: "))
    n2 = int(input("Enter your second number here: "))
    ans = n1 * n2
    print(f"{n1} x {n2} =", ans)
    return pick()
    
def division():
    n1 = int(input("Enter your first number here: "))
    n2 = int(input("Enter your second number here: "))
    ans = n1 / n2
    print(f"{n1} : {n2} =", ans)   
    return pick()

pick()