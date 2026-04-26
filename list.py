print("WELCOME TO THE LIST")

shopping_list = []

while True:

    item = input("If you want to add an item to the list type it here or say 'done' to finish:")
    if item == "done":
        break 
    else:
        shopping_list.append(item) 

print("Your shopping list is:" + str(shopping_list))