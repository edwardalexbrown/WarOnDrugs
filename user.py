import abcEconomics as abce
import math


class User(abce.Agent, abce.Household):
    def init(self):
        self.labor_endowment = 2
        self.utility_function = self.create_cobb_douglas_utility_function({"substance": 1})
        self.accumulated_utility = 0
        self.employer = self.id
        self._inventory._perishable.append('labor')  # TODO simplify this
        self.utility = 1



    def sell_labor(self):
        """ offers 2 units of labor to firm self.employer, for the price of 1 "money" """
        self.sell(('dealer', self.employer), "labor", quantity=2, price=1)

    def buy_goods(self):
        """ recieves the offers and accepts them one by one """
        self.substance_this_round = 0
        appetite = math.ceil(1 / self.utility)
        print(appetite)
        offersAccepted = 0
        for offer in self.get_offers("substance"):
            if (offersAccepted < appetite):
                self.accept(offer)
                self.substance_this_round += 1
                offersAccepted += 1
        print("Accepted:", offersAccepted, " offers")

    def consumption(self):
        """ consumes_everything and logs the aggregate utility. current_utiliy
        """
        for r in range(self.substance_this_round):
            self.utility *= 0.9

        self.accumulated_utility += self.utility
        self.log('HH', {'': self.accumulated_utility})
