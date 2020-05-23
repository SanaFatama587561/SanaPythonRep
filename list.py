fruit = ["Papaya","Apples","oranges","Banana","Grapes"]
vegetables =["Potato","Tomato","carrots","Raddish"]

print(fruit + vegetables) #Concatenate two list
print(fruit *3 )   #Prints list "fruit" 3 times
print(fruit[2:4])   #This will slice the list starting from 2nd index value to 4th Index value
print(len(fruit))    #This prints length of the  list
print(vegetables[2])  #this will print the element at index value 2
vegetables.insert(2,"Brinjal") #This will add an element to existing list at any specified index
print(vegetables)
vegetables.append("Chillies")  #This will add an element to the end of the end of the list
print(vegetables)

vegetables.pop(2) #this will delete an elemnet
print(vegetables)

next_item=0
fruit=iter(fruit)
for i in range(0,2):
    next_item = next_item(fruit)
    print(next_item)
