from engine.sternman_engine import SternmanEngine
from battery.splinder_battery import SplinderBattery
from car import Car

class Palindrome(Car):
    def __init__(self, warning_light_is_on, last_service_date):
        self.warning_light_is_on = warning_light_is_on
        self.last_service_date = last_service_date


    def status(self):
        engine =  SternmanEngine(self.warning_light_is_on)
        battery = SplinderBattery(self.last_service_date)