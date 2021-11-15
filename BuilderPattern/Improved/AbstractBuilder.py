from Computer import Computer
import abc

class AbstractBuilder(object):
    __metaclass__ = abc.ABCMeta

    def getComputer(self):
        return self._computer

    def newComputer(self):
        self._computer = Computer()
    
    @abc.abstractmethod
    def buildMainboard(self):
        pass

    @abc.abstractmethod
    def getCase(self):
        pass

    @abc.abstractmethod
    def installMainboard(self):
        pass

    @abc.abstractmethod
    def installHarddrive(self):
        pass

    @abc.abstractmethod
    def installVideoCard(self):
        pass