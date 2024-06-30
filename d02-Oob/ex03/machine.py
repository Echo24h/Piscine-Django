import beverages
import random

class CoffeeMachine:

    def __init__(self) -> None:
        self.obsolescence = 10


    class EmptyCup(beverages.HotBeverage):

        def __init__(self) -> None:
            super().__init__(price=0.90, name="empty cup")

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"


    class BrokenMachineException(Exception):

        def __init__(self) -> None:
            Exception.__init__(self, "This coffee machine has to be repaired.")

    
    def repair(self) -> None:
        self.obsolescence = 10
        print("The coffee machine has been repaired.")

    
    def serve(self, beverage: beverages.HotBeverage) -> beverages.HotBeverage:
        if self.obsolescence <= 0:
            raise self.BrokenMachineException()
        self.obsolescence -= 1

        if random.randint(0, 1):
            return self.EmptyCup()
        return beverage


if __name__ == "__main__":

    machine = CoffeeMachine()

    for i in range(2):
        try:
            for i in range(5):
                print(machine.serve(beverages.HotBeverage()))
                print(machine.serve(beverages.Coffee()))
                print(machine.serve(beverages.Tea()))
                print(machine.serve(beverages.Chocolate()))
                print(machine.serve(beverages.Cappuccino()))

        except machine.BrokenMachineException as e:
            print(e)
            machine.repair()