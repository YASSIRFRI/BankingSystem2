###################################################################################################################
#Program : UM6P-CS -cpi2
#Author : Yassir Fri
#Date of creation : 2022-02-11
###################################################################################################################






class Customer:
    """This represents the Custumer class"""
    def __init__(self,name,id,adress="",accounts=[]) -> None:
        self.__name=name
        self.__id=id
        self.__adress=adress
        self.__accounts=accounts

    def getName(self):
        """Returns the name of the customer"""
        return self.__name
    def getId(self):
        """Returns the id of the customer"""
        return self.__id
    def getAdress(self):
        """Returns the adress of the customer"""
        return self.__adress
    def getAccounts(self):
        """Returns the accounts of the customer"""
        return self.__accounts
    def setName(self,name):
        """Sets the name of the customer"""
        self.__name=name
        return
    def setId(self,id):
        """Sets the id of the customer"""
        self.__id=id
        return
    def setAdress(self,adress):
        """Sets the adress of the customer"""
        self.__adress=adress
        return
    def addAccount(self,account):
        """Adds an account to the customer"""
        self.__accounts.append(account)
        return
    def removeAccount(self,account):
        """Removes an account from the customer"""
        self.__accounts.remove(account)
        del account
        return
    
    

