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


# (5) type of desing
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
class ParkingSpot(Enum):
    Hadicapped = 0
    Compact = 1
    Large = 2
    Motocycle = 3



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