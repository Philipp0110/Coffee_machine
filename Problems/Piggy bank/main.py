class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        
    def add_money(self, deposit_dollars, deposit_cents):
        compare = self.cents + deposit_cents
        if compare > 99:

            self.dollars += deposit_dollars + ((deposit_cents + self.cents) // 100)
            self.cents = (deposit_cents + self.cents) % 100
        else:
            self.cents += deposit_cents
            self.dollars += deposit_dollars
