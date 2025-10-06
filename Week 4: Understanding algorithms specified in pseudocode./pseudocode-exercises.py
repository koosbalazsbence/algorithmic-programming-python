# Exercise 1

a = int(input("Enter a value for a: "))

if a < 0:
    b = -1*a
else:
    b = a

print(b)

# Example input/output:
# Enter a value for a: 10
# 10
# Enter a value for a: -4
# 4

# Explanation:
# This code computes the absolute value of the integer 'a' and stores it in 'b'.

a = int(input("Enter a value for a: "))
if a < 0:
    a = -1 * a

print(a)

# Explanation:
# This code computes the absolute value of 'a' by modifying 'a' directly.

# Exercise 2

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

c = a

while b > 0:
    c = c - 1
    b = b - 1

print(c)

# Example input/output:
# Enter a value for a: 7
# Enter a value for b: 3
# 4

# Explanation:
# This code computes the result of 'a - b' using repeated subtraction.

# Exercise 3

N = int(input("Enter a value for N: "))

R = 0

while N > 0:
    R = R * 10 + N % 10
    N = (int) (N/10)

print(R)

# Example input/output:
# Enter a value for N: 73251
# 15237

# Explanation:
# This code reverses the digits of the integer 'N' and stores the result in 'R'.

# Exercise 4

N = int(input("Enter a value for N: "))
B = int(input("Enter a value for B: "))

R = 0
P = 1

while N != 0:
    R = R + (N % B) * P
    N = (int) (N / B)
    P = P * 10

print(R)

# Example input/output:
# Enter a value for N: 15
# Enter a value for B: 2
# 1111
# Enter a value for N: 30
# Enter a value for B: 3
# 1010
# Enter a value for N: 64
# Enter a value for B: 8
# 100


# Explanation:
# This code converts the integer 'N' from decimal (base 10) to base 'B' using repeated division and multiplication.

# Exercise 5

A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))

while B > 0:
    C = B
    B = A % B
    A = C

print(A)

# Example input/output:
# Enter a value for A: 24
# Enter a value for B: 18
# 6
# Enter a value for A: 165
# Enter a value for B: 48
# 21

# Explanation:
# This code computes the greatest common divisor (GCD) of 'A' and 'B' using the Euclidean algorithm.

# Exercise 6

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

z = x * y

while y >= 1:
    w = y
    y = x % y
    x = w

print(z / x)

# Example input/output:
# Enter a value for x: 12
# Enter a value for y: 30
# 60.0
# Enter a value for x: 18
# Enter a value for y: 18
# 18.0

# Explanation:
# This code computes the least common multiple (LCM) of 'x' and 'y' using the relationship between LCM and GCD.

# Exercise 7

A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))

while A != B:
    if A > B:
        A = A - B
    else:
        B = B - A

print(B)

# Example input/output:
# Enter a value for A: 24
# Enter a value for B: 18
# 6
# Enter a value for A: 165
# Enter a value for B: 48
# 21

# Explanation:
# This code computes the greatest common divisor (GCD) of 'A' and 'B' using the subtraction-based Euclidean algorithm.

# Exercise 8 - linear congruential generator

a = int(input("Enter a value for a: "))
m = int(input("Enter a value for m: "))
x = int(input("Enter a value for x: "))
x0 = x

while 1==1:
    x = (a * x) % m
    print(x)
    if x == x0:
        break

# Example input/output:
# Enter a value for a: 16807
# Enter a value for m: 2147483647
# Enter a value for x: 1672552800
# 1914720636

# Enter a value for a: 12
# Enter a value for m: 7
# Enter a value for x: 1
# 5

# Explanation:
# This code implements a linear congruential generator (LCG) to produce a sequence of pseudo-random numbers based on the provided parameters 'a', 'm', and initial seed 'x0'. The sequence continues until it cycles back to the initial seed value.

# Exercise 9 - even or odd

num = int(input("Enter a value for num: "))

while num > 1:
    num = num - 2
    if num == 0:
        print("even")
    elif num == 1:
        print("odd")

# Example input/output:
# Enter a value for num: 10
# even
# Enter a value for num: 7
# odd

# Explanation:
# This code determines whether the input integer 'num' is even or odd by repeatedly subtracting 2 until it reaches 0 (even) or 1 (odd).

# Exercise 10 - median of three numbers

a = int(input("Enter a value for num: "))
b = int(input("Enter a value for num: "))
c = int(input("Enter a value for num: "))

if a < b:
    if a < c:
        if b < c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b < c:
        if a < c:
            print(a)
        else:
            print(c)
    else:
        print(b)

# Example input/output:
# Enter a value for num: 10
# Enter a value for num: 4
# Enter a value for num: 7
# 7
# Enter a value for num: 1
# Enter a value for num: 2
# Enter a value for num: 3
# 2

# Explanation:
# This code finds and prints the median (middle) value among the three input integers 'a', 'b', and 'c' using nested conditional statements.

# Exercise 11 - root of a number

N = float(input("Enter a value for n: "))
threshold = float(input("Enter a threshold value: "))

x = N / 2.0
while True:
    next_x = 0.5 * (x + N / x)
    if abs(next_x - x) < threshold:
        break
    x = next_x

print(next_x)

# Example input/output:
# Enter a value for n: 25
# Enter a threshold value: 0.01
# 5.000023178253949
# Enter a value for n: 2
# Enter a threshold value: 0.0001
# 1.4142135623746899

# Explanation:
# This code computes the square root of the number 'n' using the Newton-Raphson method, iterating until the change between successive approximations is less than the specified 'threshold'.