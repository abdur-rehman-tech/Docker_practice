# app.py

def divide(a, b):
    try:
        result = a / b
        print(f"Result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    print("Welcome to the Dockerized Python App!")
    divide(10, 2)
