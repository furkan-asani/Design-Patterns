class Order(object):
    def __init__(self, shipper):
        self._shiper = shipper
    
    @property
    def shipper(self):
        return self._shiper
        