day = "monday"
temp = 20
raining = False

if day == "monday" and temp > 10 and not raining:
    print("Take a trip")
else:
    print("Sit home and learn 'Python'")

if 0:   # this will always execute the false value
    print("True")
else:
    print("False")

name = input("Enter your name")
#if you enter any name it will work fine but you leave it blank it will give you the else value
if name:
     print("hello {}".format(name))
else:
     print("No name")

name=input("Enter Your Name")
age = int(input("Enter your age"))
if 18 <= age < 31:
    print("Welcome {}".format(name))

for x in "banana":
    print(x)
