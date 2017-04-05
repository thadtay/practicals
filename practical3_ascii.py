lower = 10
upper = 100


def get_number(lower, upper):
    number = 0
    while number < lower or number > upper:
        try:
            number = int(input("Enter a number ({}-{}):".format(lower, upper)))
        except ValueError:
            print("Enter a valid number!")
    return number


def main():
    print(get_number(lower, upper))


main()
