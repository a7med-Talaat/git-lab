import sys

def calculate_square(num):
    return num * num

def greet(name="User"):
    return f"Hey there, {name}! Welcome to Git Lab 2026."

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "Developer"
    print(greet(name))
    print(f"Square of 5 is: {calculate_square(5)}")

if __name__ == "__main__":
    main()
