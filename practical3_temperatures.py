def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsiusToFahrenheit()
        elif choice == "F":
            fahrenheitToCelsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheitToCelsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9
    print("Result: {:.2f} F".format(celsius))


def celsiusToFahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
