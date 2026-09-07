# Abstraction means:

# Hiding the internal details 
# Showing only what the user needs

# You use ATM
# you press withdraw

# you don't know:
# how bank server works
# how money is processed
# that is the abstraction

from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class SBI(ATM):
    def withdraw(self):
        print("Money with drawwn from SBI")

class HDFC(ATM):
    def withdraw(self):
        print("Money withdrawn from HDFC")

atm1 = SBI()
atm2 = HDFC()

atm1.withdraw()
atm2.withdraw()