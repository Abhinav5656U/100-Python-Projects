import math

def add(nums):
    return sum(nums)

def multiply(nums):
    return math.prod(nums)

def subtract(x,y):
    return x-y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError
    return x/y

def get_numbers():
    count = int(input("How many numbers would you like to add? "))
    if count < 2:
        print("please enter at least 2 numbers to add")
        return []

    nums = []
    for i in range(count):
        nums.append(float(input(f"Enter number {i+1}: ")))
        return nums

def main():
    print("Welcome to cli scientific calculator")

    while True:
        print("\nBASIC: 1.Add | 2.Subtract | 3.Multiply | 4.Divide")
        print("ADVANCED: 5.Power (x^y) | 6.Square Root | 7.e^x | 8.Log (ln/10) | 9.Trig (sin/cos/tan)")
        print("Type '0' to Quit")
        choice = input("Which operation would you like to perform?(0 to 9): ").strip()

        if choice == "0":
            print("Turning off the calculator")
            break

        if choice not in [str(i) for i in range(1, 10)]:
            print("Please enter a valid choice")
            continue

        try:
            if choice in ['1','3']:
                nums = get_numbers()
                if not nums:
                    continue

                if choice == '1':
                    print(f"Result: {add(nums)}")
                elif choice == '3':
                    print(f"Result: {multiply(nums)}")

            elif choice in ['2', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")

            elif choice == '5':
                base = int(input("Enter base: "))
                exp = int(input("Enter exponent: "))
                print(f"Result: {pow(base, exp)}")

            elif choice == '6':
                num = float(input("Enter number: "))
                if num < 0:
                    print("Please enter a number greater than zero")
                else:
                    print(f"Result: {math.sqrt(num)}")

            elif choice == '7':
                num = float(input("Enter power of e: "))
                print(f"Result: {math.exp(num)}")

            elif choice == '8':
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Error! Logarithms require numbers strictly greater than 0.")
                else:
                    log_type = input("Type 'ln' for Natural Log or '10' for Base-10 Log: ").strip().lower()
                    if log_type == 'ln':
                        print(f"Result: {math.log(num)}")
                    elif log_type == '10':
                        print(f"Result: {math.log10(num)}")
                    else:
                         print("Invalid log type.")

            elif choice == '9':
                num = float(input("Enter degrees: "))
                trig_type = input("Type 'sin', 'cos', or 'tan': ").strip().lower()
                rads = math.radians(num)

                if trig_type == 'sin':
                    print(f"Result: {math.sin(rads)}")
                elif trig_type == 'cos':
                    print(f"Result: {math.cos(rads)}")
                elif trig_type == 'tan':
                    print(f"Result: {math.tan(rads)}")
                else:
                    print("Invalid trig type.")

        except ValueError:
            print("Invalid input! Please enter valid numbers only.")

if __name__ == '__main__':
    main()


