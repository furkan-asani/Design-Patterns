class Director(object):

    def __init__(self, builder):
        self._builder = builder

    def buildComputer(self):
        self._builder.newComputer()
        self._builder.getCase()
        self._builder.buildMainboard()
        self._builder.installMainboard()
        self._builder.installHarddrive()
        self._builder.installVideoCard()

    def getComputer(self):
        return self._builder.getComputer()