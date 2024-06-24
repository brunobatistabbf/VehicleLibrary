from abc import ABC, abstractmethod

class IVehicleStorage(ABC):
    @abstractmethod
    def SaveVehicleData(self, vehicle):
        pass

