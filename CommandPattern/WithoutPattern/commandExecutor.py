class CommandExecutor(object):

    def executeCommand(self, args):
        if(args[0]) == "CreateOrder":
            self.createOrder()
        elif(args[0]) == "UpdateQuantity":
            self.updateQuantity(args[1])
        elif(args[0]) == "ShipOrder":
            self.shipOrder
        else:
            print("Unrecognized command: %s" % args[0])

    def createOrder(self):
        pass

    def updateQuantity(self, value):
        print(value)
        oldValue = 5
        print("Database Updated")
        print("Logging updated quantity from %s to %s" %(oldValue, value))

    def shipOrder(self):
        pass