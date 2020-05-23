splitString = "This string has been \nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

anotherString = """This string has been \
split over \
several \
lines"""

print(anotherString)
Name = "sana"
Age = 25
print(Name)
print(type(Name))
print(Age)
print(type(Age))
Age = "25"
print(Age)
print(type(Age))
a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

for i in range(1, a // b):
    print(i)
