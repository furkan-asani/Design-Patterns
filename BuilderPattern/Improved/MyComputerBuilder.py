from AbstractBuilder import AbstractBuilder

class MyComputerBuilder(AbstractBuilder):
    def getCase(self):
        self._computer.case = 'Coolermaster N300'

    def buildMainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'

    def installMainboard(self):
        pass

    def installHarddrive(self):
        self._computer.hardDrive = 'Seagate 2TB'

    def installVideoCard(self):
        self._computer.videoCard = 'GeForce GTX 1070'