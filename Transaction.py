###################################################################################################################
#Program : UM6P-CS -cpi2
#Author : Yassir Fri
#Date of creation : 2022-02-11
###################################################################################################################

import Money
from enum import Enum

class Transaction:
    """This represents a Transaction class"""
    def __init__(self,account,amount,id,Datetime="",status="")->None:
        self._amount=Money.Money(amount)
        self._dateTime=Datetime
        self._status=status
        self._id=id
        self._account=account

    
    def getStatus(self):
        """This method returns the Status of a class"""
        return self._status
    def getDateTime(self):
        """This method returns the Date Time of a class"""
        return self._dateTime
    def getAmount(self):
        """This method returns the Amount of a class"""
        return self._amount
    def getId(self):
        """This method returns the Id of a class"""
        return self._id
    def setId(self,id):
        """This method sets the Id of a class"""
        self._id=id
        return
    
    def setStatus(self,status):
        """This method sets the Status of a class"""
        self._status=status
        return 
    def setDateTime(self,date):
        """This method sets the Date Time of a class"""
        self._dateTime=date
        return 
    def setAmount(self,amount):
        """This method sets the Amount of a """
        self.__amount= amount
        return 
    def display(self):
        """This method returns the info of a class"""
        print("Transaction Info:")  
        print("Transaction Id : ",self._id)
        print("AccountNumber: ",self._account.getNumber())
        print("Amount: ",self._amount.getAmount())
        print("Date: ",self._dateTime)
        print("Status: ",self._status.value)
        return
    
    def begin(self):
        raise ValueError("Not yet Implemented")
    def commit(self):
        raise ValueError("Not yet Implemented")
    def rollback(self,other):
        raise ValueError("Not yet Implemented")
    
class Transfer(Transaction):
    def __init__(self,account, other, amount, id,Datetime="",status="") -> None:
        super().__init__(account,amount, id,Datetime, status)
        self._other=other
    def begin(self):
        """This method begins the transaction"""
        self._status=Status.Success
        if self._account.getBalance()-self._amount.getAmount()<self._account.getMinimum() or self._other.getBalance()-self._amount.getAmount()<self._other.getMinimum():
            self._status=Status.Rejected
            return False
        else:
            self._account.setBalance(self._account.getBalance()-self._amount.getAmount())
            self._other.setBalance(self._other.getBalance()+self._amount.getAmount())
            self._status=Status.Success
            self.commit(self._other)

            return True
    def commit(self,other=None):
        """This method commits the transaction"""
        if self._status==Status.Success:
            self._status=Status.Saved_Success
        self._account.addTransaction(self)
        self._other.addTransaction(self)
        if other!=None:
            other.addTransaction(self)
    def rollback(self,other):
        """This method rolls back the transaction"""
        self._account.setBalance(self._account.getBalance()+self._amount)
        self._other.setBalance(self._other.getBalance()-self._amount)
        self._status=Status.Failed
        self.commit()
        return True
    def getInfo(self):
        print("Transfer Info:")  
        print("From: ",self._account.getNumber())
        print(" To: ",self._other.getNumber())
        print("Amount: ",self._amount.getAmount())
        print("Date: ",self._dateTime)
        print("Status: ",self._status.value)
        return
    
        

class Witdraw(Transaction):
    def __init__(self,account, amount, id,Datetime="", status="") -> None:
        super().__init__(account,amount, id,Datetime, status)
    def begin(self):
        """This method begins the transaction"""
        self._status=Status.InProgress
        if self._account.getBalance()-self._amount.getAmount()<self._account.getMinimum():
            self._status=Status.Rejected
            return False
        else:
            self._account.setBalance(self._account.getBalance()-self._amount.getAmount())
            self._status=Status.Success
            self.commit()
            return True
    def rollback(self):
        """This method rolls back the transaction"""
        self._account.setBalance(self._account.getBalance()+self._amount.getAmount())
        self._status=Status.Cancelled
        self.commit()
        return True
    def commit(self):
        """This method commits the transaction"""
        self._status=Status.Saved_Cancelled
        self._account.addTransaction(self)
        return True



class Deposit(Transaction):
    """This represents a Deposit transaction"""
    def __init__(self,account, amount, id,Datetime="", status="") -> None:
        super().__init__(account,amount, id,Datetime, Status.InProgress)

    def begin(self):
        """This method begins the transaction"""
        self._status=Status.InProgress
        self._account.setBalance((self._account.getBalance()+self._amount.getAmount()))
        self._status=Status.Success
        self.commit()
        return True
    def rollback(self):
        """This method rolls back the transaction"""
        self._account.setBalance((self._account.getBalance()-self._amount.getAmount()))
        self._status=Status.Cancelled
        self.commit()
        return True
    def commit(self):
        """This method commits the transaction"""
        if self._status==Status.Success:
            self._status=Status.Saved_Success
        self._account.addTransaction(self)
        return True



class Status(Enum):
    """This represents a Status Enum"""
    InProgress="In progress"
    Success="Success"
    Rejected="Rejected"
    Cancelled="Cancelled"
    Saved="Saved"
    Saved_Cancelled="Saved Cancelled"
    Saved_Success="Saved Success"








