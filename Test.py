###################################################################################################################
#Program : UM6P-CS -cpi2
#Author : Yassir Fri
#Date of creation : 2022-02-11
###################################################################################################################


import Account
import Money
import Customer
import datetime





customer1=Customer.Customer("Yassir","001","CCI",)
customer2=Customer.Customer("Zakaria","002","CCI",)
account1=Account.CheckingAccount("001",1000,customer1)
account2=Account.SavingsAccount("002",3500,customer2,2000,0.05)
print("***Customer1***")
customer1.display()


print("***Account1***")
account1.display()
print("***Sample transactions***")
account1.deposit(100)
account1.getHistory()[0].display()
print(account1.getBalance())
account1.withdraw(200)
account1.getHistory()[1].display()
print(account1.getBalance())

account1.sendMoney(account2,100)
account1.getHistory()[2].display()
print(account1.getBalance())
print(account2.getBalance())

print("***Testing the rollback feature***")
account3=Account.SavingsAccount("003",2500,customer1,2000,0.05)
account3.display()
account3.deposit(100)
account3.withdraw(200)
account3.cancelTransaction(account3.getHistory()[-1].getId()) #Cancels the last transaction
account3.display() #final balance should be 2600

account3.sendMoney(account2,100)
account3.display()
account2.display()
account3.cancelTransaction(account3.getHistory()[-1].getId()) #Cancels the last Transfer
account3.display() #final balance should return to  2600
account2.display() #final balance should return to  3600














