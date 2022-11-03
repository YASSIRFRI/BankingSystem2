import Account
import Money
import Customer





customer1=Customer.Customer("Yassir","001","CCI",)
customer2=Customer.Customer("Zakaria","002","CCI",)
account1=Account.CheckingAccount("001",1000,customer1)
account2=Account.SavingsAccount("002",3500,customer2,2000,0.05)
account1.deposit(100)
account1.getHistory()[0].getInfo()
print(account1.getBalance())
account1.withdraw(200)
account1.getHistory()[1].getInfo()
print(account1.getBalance())

account1.sendMoney(account2,100)
account1.getHistory()[2].getInfo()
print(account1.getBalance())
print(account2.getBalance())










