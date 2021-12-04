import abcEconomics as abce


class Dealer(abce.Agent, abce.Firm):
    def init(self):
        self.price = {}
        self.create('money', 4)
        self.inputs = {"labor": 1}
        self.output = "some_crack"
        self.outquatity = 2
        self.price['some_crack'] = 1

        self.pf = self.create_cobb_douglas(self.output, self.outquatity, self.inputs)

    def buy_inputs(self):
        oo = self.get_offers("labor")
        for offer in oo:
            self.accept(offer)

    def production(self):
        self.produce(self.pf, self.inputs)

    def sell_goods(self):
        """ 
        sell some some crack to each of 2 addicts
        """
        for i in range(2):
            self.sell(('addict', i), 'some_crack', price=1, quantity=1)
