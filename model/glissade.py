from engine.willoughby_engine import WilloughbyEngine
from battery.splinder_battery import SplinderBattery
from car import Car

class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date


    def status(self):
        engine =  WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SplinderBattery(self.last_service_date)