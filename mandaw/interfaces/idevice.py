from abc import ABC, abstractmethod


class IDevice(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def pressed(self):
        pass

    @abstractmethod
    def get_info(self) -> dict:
        return {}

    @abstractmethod
    def disconnect(self):
        pass
