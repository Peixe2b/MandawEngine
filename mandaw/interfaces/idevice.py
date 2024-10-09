from abc import ABC, abstractmethod


class IDevice(ABC):
    @abstractmethod
    def press(self, input):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_info(self) -> dict:
        return {}

