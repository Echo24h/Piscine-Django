class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."


# Test the Intern and Coffee classes
if __name__ == "__main__":
    # Instantiate Intern without a name
    intern1 = Intern()
    print(intern1)

    # Instantiate Intern with the name "Mark"
    intern2 = Intern("Mark")
    print(intern2)

    # Ask Mark to make a coffee
    coffee = intern2.make_coffee()
    print(coffee)

    # Ask the first intern to work and handle the exception
    try:
        intern1.work()
    except Exception as e:
        print(e)