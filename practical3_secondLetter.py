def main():
    frequency = 2
    name = get_name()
    printName(name, frequency)


def printName(name, frequency):
    for x in range(1, len(name), frequency):
        print(name[x])


def get_name():
    name = input("Enter a name:")
    return name


main()
