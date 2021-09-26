from Shipper import Shipper

class ShippingCost(object):
    def shippingCost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedexCost(order)
        elif order.shipper == Shipper.ups:
            return self._upsCost(order)
        elif order.shipper == Shipper.postal:
            return self._postalCost(order)
        else:
            raise ValueError('Invalid shipper %s', order.shipper)
    def _fedexCost(self, order):
        return 3
    def _upsCost(self, order):
        return 4
    def _postalCost(self, order):
        return 5