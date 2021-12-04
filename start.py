""" Agents are now build according
to the line in agents_parameter.csv
"""
from abcEconomics import Simulation
from dealer import Dealer
from user import User
from user import User


simulation_parameters = {'name': 'name',
                         'trade_logging': 'off',
                         'random_seed': None,
                         'rounds': 10}

def main(simulation_parameters):
    print("Let the simulation..... commence")	

    simulation = Simulation()

    try:
        dealers = simulation.build_agents(Dealer, 'dealer', 2)
        users = simulation.build_agents(User, 'user', 2)

        for r in range(simulation_parameters['rounds']):
            print("----------------", r ,"-------------------")
            simulation.advance_round(r)
            users.refresh_services('labor', derived_from='labor_endowment', units=5)
            # to access round, just get the value of w.round
            # to access its datetime version, use w._round # todo, better naming
            users.sell_labor() 
            dealers.buy_inputs() 
            dealers.production()
            dealers.panel_log(goods=['substance'])
            dealers.sell_goods()
            users.buy_goods()
            users.panel_log(goods=['substance'])
            users.consumption()
    
    finally:
        simulation.finalize()


if __name__ == '__main__':
    main(simulation_parameters)
