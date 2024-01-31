class Bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    
    def deposit(self,amount):
        self.balance += amount  
    
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
    
    def check(self):
        print(self.owner,self.balance)
        
account = Bank("Ali",10000)
account.deposit(1000)
account.deposit(500)

account.check()

account.withdraw(2300)
account.withdraw(4000)

account.check()


        
    