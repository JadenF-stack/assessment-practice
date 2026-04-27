print("Welcome to the shopping list program!")

shopping_list = [] 

while True:

    item = input("say done if you dont want to add to list!")
    if item == "done":
        break
    else:
        shopping_list.append(item)

print("Your shopping list is:" + str(shopping_list))