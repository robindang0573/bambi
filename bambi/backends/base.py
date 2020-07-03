from abc import ABCMeta, abstractmethod


class BackEnd:
    """Base class for BackEnd hierarchy."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def run(self):
        pass
