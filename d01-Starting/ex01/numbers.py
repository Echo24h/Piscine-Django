
def numbers(filename : str = 'numbers.txt') -> None:
    with open(filename, 'r') as f:
        content = f.read().strip()
        numbers = content.split(',')
        for n in numbers:
            print(n)


if __name__ == '__main__':
    numbers()