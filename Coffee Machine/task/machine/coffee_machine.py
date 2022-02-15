import math

class CoffeeMachine:

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money
"""

    def calc_coffee(self, style):
        w = self.water
        m = self.milk
        b = self.beans
        c = self.cups

        out_w = 'Sorry, not enough water!\n'
        out_m = 'Sorry, not enough milk!\n'
        out_b = 'Sorry, not enough beans!\n'
        out_c = 'Sorry, not enough cups!\n'

        if style == '1':
            w -= 250
            b -= 16
            c -= 1
            if w < 0:
                print(out_w)
                return False
            elif b < 0:
                print(out_b)
                return False
            elif c < 0:
                print(out_c)
                return False
        elif style == '2':
            w -= 350
            m -= 75
            b -= 20
            c -= 1
            if w < 0:
                print(out_w)
                return False
            elif m < 0:
                print(out_m)
                return False
            elif b < 0:
                print(out_b)
                return False
            elif c < 0:
                print(out_c)
                return False
        elif style == '3':
            w -= 200
            m -= 100
            b -= 12
            c -= 1
            if w < 0:
                print(out_w)
                return False
            elif m < 0:
                print(out_m)
                return False
            elif b < 0:
                print(out_b)
                return False
            elif c < 0:
                print(out_c)
                return False

        print("I have enough resources, making you a coffee!\n")

        return True

    def do_something(self, ):
        while True:

            action = input("Write action (buy, fill, take, remaining, exit):\n")

            if action == 'exit':
                break
            elif action == 'remaining':
                print(self)
            elif action == 'buy':
                kind = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

                if kind == 'back':
                    print()
                    continue

                if not self.calc_coffee(kind):
                    continue

                if kind == '1':
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
                elif kind == '2':
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
                elif kind == '3':
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6
            elif action == 'fill':
                add_water = int(input("\nWrite how many ml of water you want to add:\n"))
                add_milk = int(input("Write how many ml of milk you want to add:\n"))
                add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
                add_cups = int(input("Write how many disposable cups of coffee you want to add:\n"))
                print()

                self.water += add_water
                self.milk += add_milk
                self.beans += add_beans
                self.cups += add_cups
            elif action == 'take':
                print(f"\nI gave you ${self.money}\n")
                self.money = 0

    def calc_cups(self, requested):
        """This function takes a requested amount of coffee and prints out what can be done
        given the available resources.
        """

        water_p = 1 / 200 * self.water
        milk_p = 1 / 50 * self.milk
        beans_p = 1 / 15 * self.beans

        least = math.floor(min([water_p, milk_p, beans_p]))

        if least > requested:
            print(f"Yes, I can make that amount of coffee (and {least - requested} more than that)")
        elif least == 1:
            print("Yes, I can make that amount of coffee")
        else:
            print(f"No, I can only make {least} cups of coffee")


cm = CoffeeMachine()

cm.do_something()
