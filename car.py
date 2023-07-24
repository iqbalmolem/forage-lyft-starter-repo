from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def status(self):
        pass 

    def need_service(self):
        battery_service_status, engine_service_status = self.status()
        for i in [battery_service_status, engine_service_status]:
            if i:
                return True 
            else:
                return False 
