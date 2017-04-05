import random

quickPicks = int(input("How many 'quick picks' do you wish to generate: "))

counter = 6

while quickPicks > 0:
    listy = []
    while counter > 0:
        listy.append(random.randint(0,45))
        counter -= 1
    print(listy)
    counter = 6
    quickPicks -= 1

    