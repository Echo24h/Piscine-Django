import sys


def get_capital_city(loc_name: str, states: dict, capital_cities: dict) -> str:
    lower_states = {k.lower(): v for k, v in states.items()}
    if loc_name in lower_states:
        return capital_cities[lower_states[loc_name]]
    else:
        return None


def get_state(loc_name: str, states: dict, capital_cities: dict) -> str:
    lower_inverted_capital_cities = {v.lower(): k for k, v in capital_cities.items()}
    inverted_states = {v: k for k, v in states.items()}
    if loc_name in lower_inverted_capital_cities:
        return inverted_states[lower_inverted_capital_cities[loc_name]]
    else:
        return None


def all_in() -> None:
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
    if len(sys.argv) != 2:
        return
    args = [arg.strip() for arg in sys.argv[1].split(',') if arg.strip()]
    
    for v in args:
        state = get_state(v.lower(), states, capital_cities)
        capital_city = get_capital_city(v.lower(), states, capital_cities)
        if state:
            print(f"{v.title()} is the capital of {state}")
        elif capital_city:
            print(f"{capital_city} is the capital of {v.title()}")
        else:
            print(f"{v} is neither a capital city nor a state")


if __name__ == '__main__':
    all_in()