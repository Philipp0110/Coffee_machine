# Write your code here
class CoffeeMachine:
    machine_water = None
    machine_milk = None
    machine_grams = None
    machine_cups = None
    machine_money = None
    machine_on = True
    machine_state = "menu"

    def __init__(self, water, milk, grams, cups, money):
        self.machine_water = water
        self.machine_milk = milk
        self.machine_grams = grams
        self.machine_cups = cups
        self.machine_money = money

    def __str__(self):
        print("The coffee machine has:")
        print("{water} of water".format(water=self.machine_water))
        print("{milk} of milk".format(milk=self.machine_milk))
        print("{grams} of coffee beans".format(grams=self.machine_grams))
        print("{cups} of disposable cups".format(cups=self.machine_cups))
        print("{money} of money".format(money=self.machine_money))

    def print_user_action(self):
        if self.machine_state == "menu":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.machine_state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    def state_switcher(self, input):
        if self.machine_state == "menu":
            if input == "buy":
                self.machine_state = "buy"
            elif input == "fill":
                self.fill_machine()
                self.machine_state = "menu"
            elif input == "take":
                self.take_money()
                pass
            elif input == "remaining":
                self.__str__()
                pass
            elif input == "exit":
                self.machine_set()
                pass
            else:
                print("Invalid input")
        elif self.machine_state == "buy":
            if input == "back":
                self.machine_state = "menu"
                pass
            elif input == "1":
                if self.check_if_enough(espresso):
                    print("I have enough resources, making you a coffee!")
                    self.change_machine_values(espresso)
                self.machine_state = "menu"
            elif input == "2":
                if self.check_if_enough(latte):
                    print("I have enough resources, making you a coffee!")
                    self.change_machine_values(latte)
                self.machine_state = "menu"
            elif input == "3":
                if self.check_if_enough(cappuccino):
                    print("I have enough resources, making you a coffee!")
                    self.change_machine_values(cappuccino)
                self.machine_state = "menu"
            else:
                print("Invalid input")
        else:
            print("Invalid input")

    def check_if_enough(self, lst):
        if self.machine_water < lst[0]:
            print("Sorry, not enough water!")
        elif self.machine_milk < lst[1]:
            print("Sorry, not enough milk!")
        elif self.machine_grams < lst[2]:
            print("Sorry, not enough coffee beans!")
        elif self.machine_cups < 1:
            print("Sorry, not enough biodegradable cups")
        else:
            return True

    def fill_machine(self):
        print("Write how many ml of water do you want to add:")
        self.machine_water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.machine_milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.machine_grams += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.machine_cups += int(input())

    def change_machine_values(self, lst):
        self.machine_water -= lst[0]
        self.machine_milk -= lst[1]
        self.machine_grams -= lst[2]
        self.machine_money += lst[3]
        self.machine_cups -= 1

    def take_money(self):
        print("I gave you {money}".format(money=self.machine_money))
        self.machine_money = 0

    def machine_set(self):
        if self.machine_on:
            print("Bye")
            self.machine_on = False
        else:
            self.machine_on = True


espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappuccino = [200, 100, 12, 6]

machine = CoffeeMachine(400, 540, 120, 9, 550)


while machine.machine_on:
    machine.print_user_action()
    user_action = input()
    machine.state_switcher(user_action)








