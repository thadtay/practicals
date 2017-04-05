from random import randint
INITIAL_POPULATION = 1000


def main():
    print("Welcome to the Gopher Population Simulator")
    print("Starting Population:", INITIAL_POPULATION)
    population = INITIAL_POPULATION

    for x in range(1, 10):
        gophersBirth = randint(int(population * 0.1), int(population * 0.2))
        gophersDeath = randint(int(population * 0.05), int(population * 0.25))
        print("Year,", x)
        print(5 * "*")
        print(gophersBirth, "gophers were born.", gophersDeath, "died")
        population = population - gophersDeath + gophersBirth
        print("Population:", population, "\n")

main()
