from abc import  ABC, abstractmethod


class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    def fuel_type(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print ("car stopped")
    def fuel_type(self):
        print("petrol")
class bike(vehicle):
        def start(self):
          print("bike started")
        def stop(self):
          print ("bike stopped")
        def fuel_type(self):
          print("petrol")
class tesla(vehicle):
    def start(self):
        print("tesla started")
    def stop(self):
        print ("tesla stopped")
    def fuel_type(self):
        print("electric")
t=tesla()
t.fuel_type()
t.start()
t.stop()
c=car()
c.start()
c.stop()
c.fuel_type()
b=bike()
b.start()
b.stop()
b.fuel_type()                  

    