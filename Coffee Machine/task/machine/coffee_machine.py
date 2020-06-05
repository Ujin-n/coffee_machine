class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

        self.cur_state = None

    def control_panel(self, input_signal=None):
        if input_signal is None:
            print("Write action (buy, fill, take, remaining, exit):")
            self.cur_state = 'main'
            return
        if self.cur_state == 'main':
            if input_signal == 'remaining':
                self.machine_state()
            elif input_signal == 'buy':
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.cur_state = 'buy'
            elif input_signal == 'fill':
                print("Write how many ml of water do you want to add:")
                self.cur_state = 'fill_water'
            elif input_signal == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
        elif self.cur_state == 'buy':
            self.machine_buy(input_signal)
            self.cur_state = 'main'
        elif self.cur_state == 'fill_water':
            self.water += int(input_signal)
            print("Write how many ml of milk do you want to add:")
            self.cur_state = 'fill_milk'
        elif self.cur_state == 'fill_milk':
            self.milk += int(input_signal)
            print("Write how many grams of coffee beans do you want to add:")
            self.cur_state = 'fill_beans'
        elif self.cur_state == 'fill_beans':
            self.beans += int(input_signal)
            print("Write how many disposable cups of coffee do you want to add:")
            self.cur_state = 'fill_cups'
        elif self.cur_state == 'fill_cups':
            self.cups += int(input_signal)
            self.cur_state = 'main'

    def machine_buy(self, input_signal):
        if self.cups - 1 < 0:
            print("Sorry, not enough cups!")
            return
        if input_signal == '1':
            if self.water - 250 < 0:
                print("Sorry, not enough water!")
                return
            elif self.beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
                return
            else:
                print("I have enough resources, making you a coffee!")
                self.cups -= 1
                self.water -= 250
                self.beans -= 16
                self.money += 4
                return
        elif input_signal == '2':
            if self.water - 350 < 0:
                print("Sorry, not enough water!")
                return
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
                return
            elif self.beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
                return
            else:
                print("I have enough resources, making you a coffee!")
                self.cups -= 1
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                return
        elif input_signal == '3':
            if self.water - 200 < 0:
                print("Sorry, not enough water!")
                return
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
                return
            elif self.beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
                return
            else:
                print("I have enough resources, making you a coffee!")
                self.cups -= 1
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                return

    def machine_state(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money".format(self.money))


coffee_machine = CoffeeMachine()
while True:
    coffee_machine.control_panel()
    action = input('> ')
    if action == 'exit':
        break
    elif action == 'remaining':
        coffee_machine.control_panel(action)
    elif action == 'buy':
        coffee_machine.control_panel(action)
        action = input('> ')
        if action == 'back':
            continue
        coffee_machine.control_panel(action)
    elif action == 'fill':
        coffee_machine.control_panel(action)
        action = input('> ')
        coffee_machine.control_panel(action)
        action = input('> ')
        coffee_machine.control_panel(action)
        action = input('> ')
        coffee_machine.control_panel(action)
        action = input('> ')
        coffee_machine.control_panel(action)
    elif action == 'take':
        coffee_machine.control_panel(action)
