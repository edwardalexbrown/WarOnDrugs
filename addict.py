import abcEconomics as abce


class Addict(abce.Agent, abce.Household):
    def init(self):
        self.labor_endowment = 2
        self.utility_function = self.create_cobb_douglas_utility_function({"some_crack": 1})
        self.accumulated_utility = 0
        self.employer = self.id
        self._inventory._perishable.append('labor')  # TODO simplify this

    def sell_labor(self):
        """ offers 2 units of labor to firm self.employer, for the price of 1 "money" """
        self.sell(('dealer', self.employer), "labor", quantity=2, price=1)

    def buy_goods(self):
        """ recieves the offers and accepts them one by one """
        for offer in self.get_offers("some_crack"):
            self.accept(offer)

    def consumption(self):
        """ consumes_everything and logs the aggregate utility. current_utiliy
        """
        current_utiliy = self.consume(self.utility_function, ['some_crack'])
        self.accumulated_utility += current_utiliy
        self.log('HH', {'': self.accumulated_utility})
