# # abstraction
#
# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#     @abstractmethod
#     def probeg(self):
#         pass
#
#     @abstractmethod
#     def year(self):
#         pass
#
#
# class Tesla(Car):
#     def probeg(self):
#         pass
#
#     def year(self):
#         pass
#
#
# car = Tesla()
# car.year()


# from abc import ABC, abstractmethod
#
#
# class Box(ABC):
#     @abstractmethod
#     def lenta(self):
#         pass
#
# class Box2(Box):
#     def lenta(self):
#         return "red"
#
# class Box3(Box):
#     def lenta(self):
#         return "blue"
#
#
# box = Box2()
# print(box.color())


# from abc import ABC, abstractmethod
#
#
# class BatteryPowered(ABC):
#     def __init__(self, battery_type):
#         self.battery_type = battery_type
#
#     @abstractmethod
#     def power_source(self):
#         pass
#
#
# class PlugPowered(BatteryPowered):
#     def __init__(self, battery_type, voltage):
#         super().__init__(battery_type)
#         self.voltage = voltage
#
#     def power_source(self):
#         return "Electr car"
#
# obj = PlugPowered("nmadr","220")
# print(obj.power_source())
#
#
