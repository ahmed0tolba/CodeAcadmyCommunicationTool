# import math 
# A = int(input('Please enter an integer for A: '))
# B = int(input('Please enter an integer for B: '))
# if A<=0:
#     print("error A must be more than 0")
# elif B<=0:
#     print("error B must be more than 0")
# else:
#     C = math.tan(B * 2 / (A * 4))
#     print('The C value is:', C)


import math

# Ask the user to enter two integer numbers
# A = int(input("Enter the value of A: "))
# B = int(input("Enter the value of B: "))

# Calculate C using the formula with eval()
C = eval("math.tan(2 * 2 / (1 * 4))")
C1 = math.tan(2 * 2 / (1 * 4))

# Print the value of C
print("C =", C , math.pi/2,C1)