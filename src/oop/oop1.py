# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#This is Parent
class Vehicle:
    pass

# Child of Vehicle


class GroundVehicle(Vehicle):
    pass

# Child of Ground Vehicle


class Car(GroundVehicle):
    pass

# Child of Ground Vehicle


class Motorcycle(GroundVehicle):
    pass

# Child of Vehicle


class FlightVehicle(Vehicle):
    pass

# Child of Flight Vehicle


class Starship(FlightVehicle):
    pass

# Child of Flight Vehicle


class Airplane(FlightVehicle):
    pass
