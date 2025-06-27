def add(x, y):
    return x + y

print ("Welcome to the Calculator!")
print("Select operation:")
prinit("1. Add")

choice = input("Enter choice (1): ")

if choice in ['1'] and choice.isdigit():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")