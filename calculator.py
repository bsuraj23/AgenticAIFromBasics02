def add(a, b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
def main():
    print("This is a simple calculator program.")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
choice = input("Enter choice(1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Invalid Input")
    print("Please enter a valid operation.")
main()
    
    
