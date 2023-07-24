from battery import Battery
from abc import ABC
from datetime import datetime

class SplinderBattery(Battery, ABC):
    def _init_(self, last_service_date):
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

    def needs_service():
        return self.service_threshold_date < datetime.today().date()