#Swapping of variable without using third variable.

a=10
b=20

print(f"The value of a is {a} & the value of b is {b} before swapping")

a=a+b  #a=30
b=a-b  #b=30-20=10
a=a-b  #a=30-10=20

print(f"The value of a is {a} & the value of b is {b} after swapping")