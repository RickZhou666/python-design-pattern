# https://www.youtube.com/watch?v=tVRyb4HaHgw&ab_channel=ThinkSoftware
# https://rickzhou905616.invisionapp.com/freehand/OOP-design-6SSnOtkl7


# (1)  requirements 

# (2) deisng pattern
#   (2.1) creational
#   (2.2) structure
#   (2.3) behavioural


# (3) design way
#   (3.1) top-down design
#           high level deisng -> subcomponent -> subcomponent -> ...

#   (3.2) bottom-up design
#           smallest component -> bigger -> bigger -> ,,,,  

# (4) Objects
#   (4.1) Parking lot system
#   (4.2) Entry/ Exit Terminals
#           - printers
#           - payment prcoessor
#   (4.3) Parking Spot
#   (4.4) Ticket
#   (4.5) Database
#   (4.6) Monitoring System


# (5) type of design
#   (5.1) singleton - for parking lot system, cuz there will be only one system
#   (5.2) factory   - to initiate instances for all of those instances


# (x) design pattern mentioned
#   (x.1) Strategy
#   (x.2) Observer
#   (x.3) Singleton
#   (x.4) factory


# =============================================================================================

from abc import abstractmethod
from enum import Enum


# This is a big NO-NO, you violate open/closed principle. when add new functionality, use extenstion instead of modification
# ==================== DONT DEFINE PARKING LOT IN THIS FASHISON START ====================
class ParkingSpot(Enum):
    Hadicapped = 0
    Compact = 1
    Large = 2
    Motocycle = 3
# ==================== DONT DEFINE PARKING LOT IN THIS FASHISON END ====================


# ==================== define parking lot start ====================
# open/closed principle
class ParkingLot():
    def __init__(self, id) -> None:
        self.id

class CompactParkingLot(ParkingLot):
    def __init__(self, id) -> None:
        super().__init__(id)
class LargeParkingLot(ParkingLot):
    def __init__(self, id) -> None:
        super().__init__(id)
class MotocycleParkingLot(ParkingLot):
    def __init__(self, id) -> None:
        super().__init__(id)
class HadicappedParkingLot(ParkingLot):
    def __init__(self, id) -> None:
        super().__init__(id)
# ==================== define parking lot end ====================

# ==================== define parking ticket start ====================
class ParkingTicket():
    def __init__(self, id, parking_spot_id, parking_spot_type, issue_time) -> None:
        self.id = id
        self.parking_spot_id = parking_spot_id
        self.parking_spot_type = parking_spot_type
        self.issue_time = issue_time
        
# ==================== define parking ticket end ====================



# ==================== define terminal start ====================
class Terminal():
    def get_id(self) -> None:
        pass

class EntryTerminal(Terminal):
    def get_ticket(parking_spot_type) -> None:
        pass
    
class ExitTerminal(Terminal):
    def accept_ticket(ticket_id):
        pass
# ==================== define terminal end ====================


# ==================== define parking assignment strategy start ====================
class ParkingAssignmentStrategy():
    @abstractmethod
    def get_parking_spot(terminal):
        pass

    @abstractmethod
    def release_parking_spot(spot):
        pass

class ParkingSpotNearEntranceStrategy(ParkingAssignmentStrategy):
    def get_parking_spot(terminal):
        return super().get_parking_spot()
    
    def release_parking_spot(spot):
        return super().release_parking_spot()

class ParkingSpotNearElevatorAndEntranceStrategy(ParkingAssignmentStrategy):
    def get_parking_spot(terminal):
        return super().get_parking_spot()
    
    def release_parking_spot(spot):
        return super().release_parking_spot()
# ==================== define parking assignment strategy end ====================


# ==================== define Payment process start ====================
class PaymentProcess:
    @abstractmethod
    def process(amount):
        pass
class CreditCardPaymentProcess(PaymentProcess):
    def process(amount):
        return super().process()

class CashPaymentProcess(PaymentProcess):
    def process(amount):
        return super().process()
# ==================== define Parment process end ====================


# ==================== define tariff calculator start ====================
class TariffCalculator():
    def calculate_tariff(time, spot_type):
        pass
# ==================== define tariff calculator end ====================
    
