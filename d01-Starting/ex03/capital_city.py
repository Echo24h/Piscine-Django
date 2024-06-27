import sys


def capital_city() -> None:
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if sys.argv[1] in states:
        print(capital_cities[states[sys.argv[1]]])
    else:
        print("Unknown state")


def main() -> None:
    if len(sys.argv) != 2:
        return
    capital_city()


if __name__ == '__main__':
    main()