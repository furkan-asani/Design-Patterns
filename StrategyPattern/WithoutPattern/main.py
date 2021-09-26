from Order import Order
from Shipper import Shipper
from ShippingCost import ShippingCost

# Here are some things which can be improved.
# - The shipper should definitely be decoupled from the order
# - Instead of having to change the implementation of the 
# shippingCost method in the ShippingCost class 
# we want to add shipping methods more flexibly
# The strategy pattern helps with both!

# Test FedEx

order = Order(Shipper.fedex)
costCalculator = ShippingCost()
costs = costCalculator.shippingCost(order)
assert costs == 3

# Test UPS

order = Order(Shipper.ups)
costCalculator = ShippingCost()
costs = costCalculator.shippingCost(order)
assert costs == 4

# Test Postal Service

order = Order(Shipper.postal)
costCalculator = ShippingCost()
costs = costCalculator.shippingCost(order)
assert costs == 5

print("All tests have passed!")