from ShippingCost import ShippingCost
from AbsStrategy import AbsStrategy
from UPSStrategy import UPSStrategy
from FedExStrategy import FedExStrategy
from PostalStrategy import PostalServiceStrategy
from Order import Order

# This is the main.py with the implemented Strategy Pattern
# The Strategy pattern is especially useful if you face a long if else statement or if you want to encapsulate
# a range of algorithms which all take the same input and return the same output
# Instead of hardcoding the logic into the ShippingCost Class we pass an object
# This enables us to fulfill the open/closed principle and makes adding new shipment services easier
# because the ShippingCost class doesn't have to be changed anymore  

sampleOrderOne = Order()
upsStrategy = UPSStrategy()
costCalculator = ShippingCost(upsStrategy)
costs = costCalculator.shipping_cost(sampleOrderOne)
assert costs == 3

sampleOrderTwo = Order()
fedExStrategy = FedExStrategy()
costCalculator = ShippingCost(fedExStrategy)
costs = costCalculator.shipping_cost(sampleOrderTwo)
assert costs == 4

sampleOrderThree = Order()
postalStrategy = PostalServiceStrategy()
costCalculator = ShippingCost(postalStrategy)
costs = costCalculator.shipping_cost(sampleOrderThree)
assert costs == 5

print("All Tests passed!")
