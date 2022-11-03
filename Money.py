class Money:
    """This reprents the Money class"""

    def __init__(self, amount, currency="MAD") -> None:
        self.__amount=amount
        self.__currency=currency
    
    def getAmount(self):
        """Returns the amount of the money"""
        return self.__amount
    def getCurrency(self):
        """Returns the currency of the money"""
        return self.__currency
    def setAmount(self,amount):
        """Sets the amount of the money"""
        self.__amount=amount
    def setCurrency(self,currency):
        """Sets the currency of the money"""
        self.__currency=currency
    def __add__(self,other):
        """Adds the amount of two money objects"""
        if self.__currency==other.getCurrency():
            return Money(self.__amount+other.getAmount(),self.__currency)
        else:
            raise ValueError("Currency does not match")
    def __sub__(self,other):
        """Subtracts the amount of two money objects"""
        if self.__currency==other.getCurrency():
            return Money(self.__amount-other.getAmount(),self.__currency)
        else:
            raise ValueError("Currency does not match")
    def __ge__(self,other):
        """Checks if the amount of the first money object is greater or equal to the amount of the second money object"""
        if self.__currency==other.getCurrency():
            return self.__amount>=other.getAmount()
        else:
            raise ValueError("Currency does not match")
    def __le__(self,other):
        """Checks if the amount of the object is less than or equal to the amount of the second object """
        if self.__currency==other.getCurrency():
            return self.__amount<=other.getAmount()
        else:
            raise ValueError("Currency does not match")

