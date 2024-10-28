def add(x, y):
    """
    Returns the sum of x and y.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Returns the difference of x and y.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The difference of x and y.
    """
    return x - y

def multiply(x, y):
    """
    Returns the product of x and y.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Returns the quotient of x and y. If y is 0, returns an error message.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float or str: The quotient of x and y, or an error message if y is 0.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    """
    The main function that drives the CLI calculator. It prompts the user to select an operation and input two numbers,
    then performs the selected operation and displays the result.
    """
    print("Simple CLI Calculator by @CodeByTomas")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
