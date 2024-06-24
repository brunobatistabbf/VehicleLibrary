from abc import ABC, abstractmethod

class IVehicleStorage(ABC):
    @abstractmethod
    def saveVehicleData(self, vehicle):
        pass

