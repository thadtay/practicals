def main():
    score = int(input("Enter score: "))
    print(getGrade(score))


def getGrade(score):
    if 50 < score <= 90:
        return "Passable"
    elif 90 < score <= 100:
        return "Excellent"
    elif 0 <= score <= 50:
        return "Bad"
    else:
        return "Invalid Input"


main()
