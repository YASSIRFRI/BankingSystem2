###################################################################################################################
#Program : UM6P-CS -cpi2
#Author : Yassir Fri
#Date of creation : 2022-02-11
###################################################################################################################

import Money
import Transaction
import Customer

class Account:
    """This represents an Account class"""
    def __init__(self,number,balance,customer: Customer,minimum=0,transaction=[]) -> None:
        self.custumer=customer
        self._number=number
        self._balance=Money.Money(balance)
        self._minimum=minimum
        self._transaction=[]
    
    def getNumber(self):
        """Returns the number of the account"""
        return self._number
    def getBalance(self):
        """Returns the balance of the account"""
        return self._balance.getAmount()
    def getMinimum(self):
        """Returns the minimum balance of the account"""
        return self._minimum
    def setBalance(self,balance):
        """Sets the balance of the account"""
        self._balance=Money.Money(balance)
        return
    def setMinimum(self,minimum):
        """Sets the minimum balance of the account"""
        self._minimum=Money.Money(minimum)
        return
    def addTransaction(self,transaction):
        """Adds a transaction to the account"""
        self._transaction.append(transaction)
    def getHistory(self):
        """Returns the history of the account"""
        return self._transaction
    def sendMoney(self,other,amount):
        """Creates a transfer transaction"""
        try:
            transfer=Transaction.Transfer(self,other,amount)
            transfer.begin()
        except:
            raise ValueError("Something went wrong")
        return 
    def withdraw(self,amount):
        """Creates a withdraw transaction"""
        try:
            print("Withdraw")
            withdraw=Transaction.Witdraw(self,amount)
            withdraw.begin()
        except:
            raise ValueError("Something went wrong")
        return
    def deposit(self,amount):
        """Creates a deposit transaction"""
        try:
            deposit=Transaction.Deposit(self,amount)
            deposit.begin()
        except:
            return False
        return True
    def cancelTransaction(self,id) :
        """Cancels a transaction"""
        for transaction in self._transaction:
            if transaction.getId()==id:
                transaction.rollback()
                return True
        return False
    



    
    

class SavingsAccount(Account):
    """This represents a SavingsAccount class"""
    def __init__(self,number,balance,customer,minimum,interestRate=0.0) -> None:
        super().__init__(number,balance,customer,minimum)
        self.__interestRate=interestRate

    def getInterestRate(self):
        """Returns the interest rate of the savings account"""
        return self.__interestRate
    def setInterestRate(self,interestRate):
        """Sets the interest rate of the savings account"""
        self.__interestRate=interestRate



class CheckingAccount(Account):
    """This represents a CheckingAccount class"""
    def __init__(self,number,balance,minimum=0) -> None:
        super().__init__(number,balance,0)


   





