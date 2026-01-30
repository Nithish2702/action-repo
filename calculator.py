#!/usr/bin/env python3
"""
Simple Calculator
A basic command-line calculator that performs arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function to run the calculator."""
    print("Welcome to Simple Calculator!")
    print("=" * 40)
    
    try:
        # Get first number
        num1 = float(input("Enter first number: "))
        
        # Get operation
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        # Get second number
        num2 = float(input("Enter second number: "))
        
        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation!")
            return
        
        # Display result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\n\nCalculator exited.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
