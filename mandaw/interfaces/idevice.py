from abc import ABC, abstractmethod


class IDevice(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def get_pressed(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass