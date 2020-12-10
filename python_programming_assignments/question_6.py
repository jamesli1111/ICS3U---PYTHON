relation_or_function = input("Which relationship would you like to see a table of values of? \n1. quadratic \n2. linear \n")

if relation_or_function == "1":

    a = float(input("Enter a value for ‘a’: "))
    b = float(input("Enter a value for ‘b’: "))
    c = float(input("Enter a value for ‘c’: ")) 

    x = (-b/(2*a)) - 6

    print(f"{'x':>11}{'y':>9}")

    for i in range(6):
        x += 1
        print(f"{round(x,1):>12}{round(a*x**2+b*x+c,1):>9}")
 
    for i in range(5):
        x += 1
        print(f"{round(x,1):>12}{round(a*x**2+b*x+c,1):>9}")


elif relation_or_function == "2":

    m = float(input("Enter a value for 'a': "))
    b = float(input("Enter a value for 'b': "))

    x = -6

    print(f"{'x':>11}{'y':>9}")

    for i in range(5):
        x += 1
        print(f"{round(x,1):>12}{round(m*x+b,1):>9}")
 
    for i in range(6):
        x += 1
        print(f"{round(x,1):>12}{round(m*x+b,1):>9}")