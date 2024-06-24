from VehicleStorageAdapter import VehicleStorageAdapter
from oldVehicleStorage import OldVehicleStorage
from vehicle import Vehicle

if __name__ == '__main__':
    old = OldVehicleStorage()
    adapter = VehicleStorageAdapter(old)
    vehicle = Vehicle("23", "Corolla", 2011)
    adapter.saveVehicleData(vehicle)

