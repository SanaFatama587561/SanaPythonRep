for i in range(1,13):
    print("No.{} square is {} and cube is {}".format(i,i**2,i**3))
print("Sana's Calculation")

name = input("let us know your name")
age = int(input("And your age too").format(name))

# If Statement

if age > 18:
    print("Hey"+ name + "You are eligible to vote")
elif age == 18:
    print("You are eligible for voting")
else:
    print("Hey Sorry" + name + "You cant vote")
answer = 10
print("please guess any number between 1 and 10:")
guess = int(input())
if guess < answer :
    print("you are close")