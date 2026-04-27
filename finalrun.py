list = []

while True:

    football_team = input("How old is everyone? Say done when finished!")
    if football_team == "done":
        break
    else:
        list.append(football_team)
print("The ages of everyone are:" + str(list))