# Extra Tips:
# 1. why use Enum?
#   In Java 1.1 type safety: Enums are strongly typed, which means that the compiler will catch any errors at compile time rather than at runtime.
#           1.2 readable: Enums provide a more readable way to define a fixed set of values

# Parking lot design part
# (1) we first define parking lot size, as normally there would be 4 type of size we can use Enum
# (2) pass LotSize instance as a variable into Lot class to create instance with a is_occupied


# Vehicle design part
# (1) base class of vehicle
# (2) subclass of different size


# function design part

# ==========================================================================================

# size of parking lot
from enum import Enum
import time


class LotSize(Enum):
    COMPACT = 1
    REGULAR = 2
    MOTOCYCLE = 3
    HANDICAPPED = 4


class Lot:
    def __init__(self, number, size: LotSize, is_occupied, parking_start_time=-1) -> None:
        self.number = number
        self.size = size
        self.occupied = is_occupied
        self.parking_start_time = parking_start_time  # unix time stamp

    def is_occupied(self):
        return self.is_occupied


# ==========================================================================================
# size of vehicle
class VehicleSize(Enum):
    COMPACT = 1
    REGULAR = 2
    MOTOCYCLE = 3


class Vehicle():
    def __init__(self, license, size, color, is_handicapped) -> None:
        self.license = license
        self.size = size
        self.color = color
        self.is_handicapped = is_handicapped


class CompactVehicle(Vehicle):
    def __init__(self, license, size, color, is_handicapped) -> None:
        super().__init__(license, size, color, is_handicapped)


class RegularVehicle(Vehicle):
    def __init__(self, license, size, color, is_handicapped) -> None:
        super().__init__(license, size, color, is_handicapped)


class Motocycle(Vehicle):
    def __init__(self, license, size, color, is_handicapped) -> None:
        super().__init__(license, size, color, is_handicapped)

# ==========================================================================================
# normally we should save data into db to check capacity, we can save inside parking garage for size tracking


class ParkingGarage:
    def __init__(self, compact_size, regular_size, motocycle_size, handicapped_size) -> None:
        self.compact_size = compact_size
        self.regular_size = regular_size
        self.motocycle_size = motocycle_size
        self.handicapped_size = handicapped_size

        self.actual_compact_size = self.compact_size
        self.actual_regular_size = self.compact_size
        self.actual_motocycle_size = self.compact_size
        self.actual_handicapped_size = self.compact_size

        self.parking_lots = []

    @property
    def total_capacity(self):
        self.total_capacity = self.compact_size + self.regular_size + \
            self.motocycle_size + self.handicapped_size

    def increase_capacity(self, lot_type: LotSize, number):
        if lot_type == LotSize.COMPACT:
            self.compact_size += number
            self.actual_compact_size += number
        elif lot_type == LotSize.REGULAR:
            self.regular_size += number
            self.actual_regular_size += number
        elif lot_type == LotSize.MOTOCYCLE:
            self.motocycle_size += number
            self.actual_motocycle_size += number
        elif lot_type == LotSize.HANDICAPPED:
            self.handicapped_size += number
            self.handicapped_size += number
        return

    # based on vehicle size to check whether parking lot availablity
    # assign lot to the car
    # (1) compact -> compact + regular, no hadicapped
    # (2) regular -> regular, no hadicapped
    # (3) hadicapped -> go hadicapped with high priority, then based on size

    def is_full(self, vehicle: Vehicle):
        if vehicle.is_handicapped:
            if self.actual_handicapped_size > 0:
                self.actual_handicapped_size -= 1
                self.parking_lots.append(
                        Lot(123, 
                            LotSize.HANDICAPPED, 
                            is_occupied=True, 
                            parking_start_time=time.time()))
            
