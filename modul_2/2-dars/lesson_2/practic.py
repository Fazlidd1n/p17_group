# 0

class BatteryPowered:
    def __init__(self , battery_type):
        self.battery_type = battery_type

    def power_source(self):
        return f"{self.battery_type}"

class PlugPowered:
    def __init__(self, voltage):
        self.voltage = voltage

    def power_source(self):
        return f"{self.voltage}"

class HybridDevice(BatteryPowered , PlugPowered):
    def __init__(self, name , battery_type , voltage):
        BatteryPowered.__init__(self, battery_type)
        PlugPowered.__init__(self, voltage)
        self.name = name

    def power_source(self):
        b = BatteryPowered.power_source(self)
        p = PlugPowered.power_source(self)
        return f"{self.name} device by {b} and {p} powered !"

obj = HybridDevice("Soch oladigan mashinka" , "lino-li" , 120)
print(obj.power_source())






