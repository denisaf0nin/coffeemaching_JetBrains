class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def remaining_checker(self, water, milk, coffee_beans):
        if (self.water >= water) and (self.milk >= milk) and (self.coffee_beans >= coffee_beans) and (self.disposable_cups >= 1):
            return True
        return False

    def decrease(self, wa, milk, coffee_beans, money):
        self.water -= wa
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.disposable_cups -= 1
        self.money += money

    def buy(self, type):
        if type == "1":
            if self.remaining_checker(250, 0, 16):
                self.decrease(250, 0, 16, 4)
                print("I have enough resources, making you a coffee!\n")
            else:
                print("Sorry, not enough water!")
        elif type == "2":
            if self.remaining_checker(350, 75, 20):
                self.decrease(350, 75, 20, 7)
                print("I have enough resources, making you a coffee!\n")
            else:
                print("Sorry, not enough water!")
        elif type == "3":
            if self.remaining_checker(200, 100, 12):
                self.decrease(200, 100, 12, 6)
                print("I have enough resources, making you a coffee!\n")
            else:
                print("Sorry, not enough water!")

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += beans
        self.disposable_cups += cups

    def take(self):
        print(f"\nI gave you ${str(self.money)}\n")
        self.money = 0

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"${self.money} of money\n")

    def action(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n> ")
            if action == "remaining":
                self.remaining()
            elif action == "buy":
                type = input("\nWhat do you want to buy? "
                            "1 - espresso, "
                            "2 - latte, "
                            "3 - cappuccino, back - to main menu:\n> ")
                self.buy(type)
            elif action == "fill":
                water = int(input("\nWrite how many ml of water do you want to add:\n> "))
                milk = int(input("Write how many ml of milk do you want to add:\n> "))
                beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
                cups = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
                print("")
                self.fill(water, milk, beans, cups)
            elif action == "take":
                self.take()
            else:
                break

CoffeeMachine(400, 540, 120, 9, 550).action()