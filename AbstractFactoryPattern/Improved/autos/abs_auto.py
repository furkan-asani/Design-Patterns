import abc


class AbstractAuto(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
