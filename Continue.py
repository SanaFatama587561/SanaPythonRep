shopping_list =["Rice","bread","apple","milk","jam"]
for item in shopping_list:
    if item == "bread":
        continue  # as soon as the compiler encounters bread it does not go to the print statement it continues
                    #it wil return to the outer loop and start executing it.
    print("Buy"+item)


shopping_list =["Rice","bread","apple","milk","jam"]
for item in shopping_list:
    if item == "bread":
        break  # as soon as the compiler encounters bread it does not go to the print statement it will break te outer loop
                #and will break rest of all the statesment after it

    print("Buy"+item)
