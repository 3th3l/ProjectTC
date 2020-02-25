def calculate_score(l):
    for i in l:
        if i[0] == i[1]:
            print("Tie")
            nl.append("Tie")
        elif i[0] == "R" and i[1] == "P":
            print("Paper beat Rock")
            nl.append("Right")
        elif i[0] == "R" and i[1] == "S":
            print("Rock beat Scissors")
            nl.append("Left")
        elif i[0] == "S" and i[1] == "P":
            print("Scissor beat Paper")
            nl.append("Left")
        elif i[0] == "S" and i[1] == "R":
            print("Rock beat Scissor")
            nl.append("Right")
        else:
            print("None")

    if nl.count("Left") > nl.count("Right"):
        print("Abigail Won")
    elif nl.count("Left") < nl.count("Right"):
        print("Benson Won")
    else:
        print("Tie")


calculate_score(list)
print(nl)