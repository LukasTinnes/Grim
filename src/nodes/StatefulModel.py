from abc import abstractmethod


class StatefulModel:

    @abstractmethod
    def compute(self):
        pass

    @abstractmethod
    def update(self):
        pass
