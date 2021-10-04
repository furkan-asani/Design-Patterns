from AbstractCommand import AbsCommand
from AbstractOrderCommand import AbsOrderCommand

class CreateOrder(AbsCommand, AbsOrderCommand):
    name = 'CreateOrder'
    description = 'CreateOrder'

    def __init__(self, args):
        pass

    def execute(self):
        #Simulate creating a new order
        print('A new order has been created!')