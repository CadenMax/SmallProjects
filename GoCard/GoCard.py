class GoCard:

    def __init__(self, current_balance):
        self.statement = []
        self.initial_balance = float(current_balance)
        self.balance = float(current_balance)
        self.count = 0

    def return_balance(self):
        print("Balance = $" + "{:.2f}".format(self.balance))

    def ride(self, amount):
        self.balance -= amount
        self.statement.append(("Ride", amount, self.balance))
        return

    def top(self, amount):
        self.balance += amount
        self.statement.append(("Top up", amount, self.balance))

    def quit(self):
        print("Statement:")
        print("{:15s} {:>12s} {:>12s}".format("event", "amount($)", "balance($)"))
        for i in self.statement:
            v1 = i[0]
            v2 = i[1]
            v3 = i[2]
            print("{:15s} {:>12.2f} {:>12.2f}".format(v1, v2, v3))


InitialBalance = float(input("Creating account. Input initial balance: "))
Balance = InitialBalance
gocard = GoCard(Balance)

Commands = input("? ")

while Commands[0] != 'q':

    Commands = Commands.split()

    if Commands[0] == 'r' and len(Commands) == 2:
        gocard.ride(float(Commands[1]))

    elif Commands[0] == 't' and len(Commands) == 2:
        gocard.top(float(Commands[1]))

    elif Commands[0] == 'b':
        gocard.return_balance()

    else:
        print("Bad Command.")

    Commands = input("? ")
gocard.quit()
