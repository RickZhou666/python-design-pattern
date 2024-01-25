# ISP


# this is a interface as we raise NotImplementedError

# instead of implement all api in one interface, you want split them separately
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError

# you can give your own code based on each methods
class MultiFunctionPrinter(Machine):
    def print(self, document):
        return super().print(document)
    
    def fax(self, document):
        return super().fax(document)
    
    def scan(self, document):
        return super().scan(document)


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass
    
    # old fashined printer cannot fax nor scan
    def fax(self, document):
        pass # do nothing
    # but there raised a question, someone initialized a old fashioned printer, 
    # but they will still see the fax or scan function
    

    
    # if this is large application, you actually CRASHING your app
    def scan(self, document):
        # but people will still see the API
        """Not supported!"""

        # this might work in small app but not ok
        raise NotImplementedError('Printer cannot scan!')


# --------------------------------------------------------------------------------------------------------

# interface
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass


# in this way, if you only want a printer
class MyPrinter(Printer):
    def print(self, document):
        print(document)

# if you want multi-function device, you will implement both interface
class Photocopier(Printer, Scanner):
    def print(self, document):
        return super().print(document)
    
    def scan(self, document):
        return super().scan(document)
    
# if you do want a multi-function device as interface, you can implement them all and override method with @abstactmethod
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    

class MultiFunctionMachine(MultiFunctionDevice):
    # build a decorator
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer


    def print(self, document):
        self.printer.print(document)
    
    def scan(self, document):
        self.scanner.scan(document)