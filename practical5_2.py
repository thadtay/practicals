colors = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000", "blanchedalmond": "#ffebcd"}

choice = input("Enter color: ")
choice = choice.lower()
while choice != "":
    if choice in colors:
        print(choice, "is", colors[choice])
    else:
        print("Invalid color")
    choice = input("Enter color: ").lower()
