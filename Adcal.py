import math
ban='''


    __   ____  _        __  __ __  _       ____  ______   ___   ____      
   /  ] /    || |      /  ]|  |  || |     /    ||      | /   \ |    \     
  /  / |  o  || |     /  / |  |  || |    |  o  ||      ||     ||  D  )    
 /  /  |     || |___ /  /  |  |  || |___ |     ||_|  |_||  O  ||    /     
/   \_ |  _  ||     /   \_ |  :  ||     ||  _  |  |  |  |     ||    \     
\     ||  |  ||     \     ||     ||     ||  |  |  |  |  |     ||  .  \    
 \____||__|__||_____|\____| \__,_||_____||__|__|  |__|   \___/ |__|\_|    

          '''                                                                
print(ban) 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number."

def sin_degrees(x):
    return math.sin(math.radians(x))

def cos_degrees(x):
    return math.cos(math.radians(x))

def tan_degrees(x):
    return math.tan(math.radians(x))

def main():
    print("Welcome to the Advanced Calculator!")
    print("Supported operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("** : Power")
    print("sqrt : Square Root")
    print("sin : Sine (in degrees)")
    print("cos : Cosine (in degrees)")
    print("tan : Tangent (in degrees)")
    print("exit : Exit the calculator")

    while True:
        user_input = input("Enter the operation or 'exit' to quit: ").strip().lower()

        if user_input == 'exit':
            print("Exiting the calculator.")
            break

        if user_input in ('+', '-', '*', '/'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if user_input == '+':
                result = add(num1, num2)
            elif user_input == '-':
                result = subtract(num1, num2)
            elif user_input == '*':
                result = multiply(num1, num2)
            elif user_input == '/':
                result = divide(num1, num2)

        elif user_input == '**':
            num1 = float(input("Enter the base: "))
            num2 = float(input("Enter the exponent: "))
            result = power(num1, num2)

        elif user_input == 'sqrt':
            num1 = float(input("Enter a number: "))
            result = square_root(num1)

        elif user_input in ('sin', 'cos', 'tan'):
            num1 = float(input("Enter an angle in degrees: "))
            if user_input == 'sin':
                result = sin_degrees(num1)
            elif user_input == 'cos':
                result = cos_degrees(num1)
            elif user_input == 'tan':
                result = tan_degrees(num1)

        else:
            print("Invalid input. Please try again.")
            continue

        print("Result:", result)

if __name__ == "__main__":
    main()
          
