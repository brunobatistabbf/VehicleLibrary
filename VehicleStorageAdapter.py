from IVehicleStorage_Interface import IVehicleStorage
class VehicleStorageAdapter(IVehicleStorage):
    def __init__(self, old_storage):
        self.old_storage = old_storage

    def saveVehicleData(self, vehicle):
        data = f"ID: {vehicle.get_id()}\nModel: {vehicle.get_model()}\nYear: {vehicle.get_year()}"
        self.old_storage.storeVehicleData(data)
