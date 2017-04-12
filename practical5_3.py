userInput = input("Enter a sentence: ")
diction = {}
listy = userInput.split(" ")
print(listy)


for word in listy:
    if word in diction:
        diction[word] += 1
    else:
        diction[word] = 1


for word in sorted(diction):
    print("{}: {}".format(word, diction[word]))

