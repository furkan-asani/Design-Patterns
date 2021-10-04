from AbstractCommand import AbsCommand
from AbstractOrderCommand import AbsOrderCommand

class ShipOrder(AbsCommand, AbsOrderCommand):
    name = 'ShipOrder'
    description = 'ShipOrder'

    def __init__(self, args):
        pass

    def execute(self):
        #Simulate shipping a particular order
        print('Your order has been shipped!')