# Conversion

T = int(input("Enter a value for T: "))

while T != 20:
    if T < 20:
        T = T - 1
    else:
        T = T + 1

print("Done")

# Another example for pseudocode structures

R = float(input("Enter a value for R: "))
i = 0
x = 0

while x <= R:
    y = 0
    while y <= R:
        if x*x+y*y == R*R:
            i = i + 1
        y = y + 1
    x = x + 1

print(4*i/((R+1)*(R+1)))

# Exercise 1

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

c = a

if b > 0:
    b = b - 1
    c = c - 1
else:
    print(c)


# Exercise 2 - Conversion

x = int(input("Enter a value for x: "))

if x == 0:
    y = 0
else:
    if x > 0:
        y = y + 1
    else:
        y = y - 1

print(y)

# Exercise 3 - Conversion

x = int(input("Enter a value for x: "))

s = 0

while x > 0:
    s = s + x
    x = x - 1

print(s)

# Exercise 4 - Conversion

x = int(input("Enter a value for x: "))

while x == 0:
    print (x)
    if x > 0:
        x = x - 1
    else:
        x = x + 1
    
print(x)