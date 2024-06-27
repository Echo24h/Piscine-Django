import sys


def state() -> None:
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
    inverted_capital_cities = {v: k for k, v in capital_cities.items()}
    inverted_states = {v: k for k, v in states.items()}
    if sys.argv[1] in inverted_capital_cities:
        print(inverted_states[inverted_capital_cities[sys.argv[1]]])
    else:
        print("Unknown capital city")


def main() -> None:
    if len(sys.argv) != 2:
        return
    state()


if __name__ == '__main__':
    main()