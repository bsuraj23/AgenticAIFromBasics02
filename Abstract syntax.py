from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method

    @abstractmethod
    def stop_engine(self):
        pass  # Abstract method
