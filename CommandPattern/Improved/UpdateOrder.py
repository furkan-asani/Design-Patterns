from AbstractCommand import AbsCommand
from AbstractOrderCommand import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'

    def __init__(self, args):
        self.newQuantity = args[1]

    def execute(self):
        oldQuantity = 5
        
        #Simulate database update
        print('Updated database')

        #Simulate logging the update
        print('Logging: Updated quantity from %s to %s ' % (oldQuantity, self.newQuantity))