name = "Parrot"
for x in name:
    print(x)
for i in range(1,10,2):
    print("i is now{}".format(i))


for i in range(1,13):
    for j in range(2,7):
        print("Sana's number is {}".format(j))
    print("Inner loop ends here")
print("Sana's New number is :{}".format(i))
print("The outer loops end too")

for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is{2}".format(j,i,i*j))
print("---------")