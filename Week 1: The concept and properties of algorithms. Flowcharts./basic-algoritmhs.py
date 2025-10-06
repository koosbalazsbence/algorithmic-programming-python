# This algorithm calculates and prints out the absolute value of an input number.

num = float(input("Enter a number: "))
if num < 0:
    num = -1 * num

print("The absolute value is:", num)

# This algorithm tells whether an integer (given as input) is an even or odd number.

print("Give the number: ")
num = int(input())
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

