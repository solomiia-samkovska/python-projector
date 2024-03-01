# STEP 1

eq = '4x^2 +4x +    (-8) =  0'
eq = eq.replace(" ", "")
eq = eq.replace("(","")
eq = eq.replace(")","")
eq = eq.replace("+","")

# get a
a = int(eq[:eq.find('x^')])
print("a:", a)

# get b
b_starts = eq[eq.find('x^2') + 3 :]
b = int(b_starts[:b_starts.find('x')])
print("b:", b)

# get c
c_starts = b_starts[b_starts.find('x') + 1 :]
c = int(c_starts[:c_starts.find('=')])
print("c:", c)


# STEP 2

# calculate x1, x2
x1 = (-b + ((b**2 - 4*a*c)**(1/2))) / (2*a)

x2 = (-b - ((b**2 - 4*a*c)**(1/2))) / (2*a)

print('x1 = ', x1)
print('x2 = ', x2)
