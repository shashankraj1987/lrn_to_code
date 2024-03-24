''' 
CreditCard Class Design 

Fields: 
    _customer
    _bank
    _account
    _balance 
    _limit

Behaviors/Methods:
    get_customer()
    get_bank()
    get_balance()
    get_account()
    make_payment(amount)
    get_limit()
    charge(price)

'''

class Creditcard:
    '''
    This Class needs following information -> 
        Customer -> String
        bank -> String
        account -> number
        balance -> number
        limit -> number:
    '''
    def __init__(self,customer,bank,account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._balance = 0
        self._limit = limit

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def charge(self,price):
        if self._balance + price > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        self._balance -= amount
    

# Extending the Credit Card Class to charge if the user overextends 
'''
Platinum Credit Card Design 
Fields: 
    _apr()

Behaviors:
    process_month()
    charge(price)*  
'''

class Pl_Creditcard(Creditcard):
    def __init__(self,customer,bank,account,limit,apr):
        super().__init__(customer,bank,account,limit)
        self._apr = apr

    def charge(self,price):
        charge_status = super().charge(price)
        if not charge_status:
            ## Charge 5 Units of Currency if Card Swiped for insufficient balance
            self._balance += 5 
            
        return charge_status

hdfc_cc = Pl_Creditcard("Shashank Raj","HDFC Bank",4362556678941258,7000,.14)
hdfc_cc.charge(2500)
hdfc_cc.charge(5000)
print(hdfc_cc.get_balance())


