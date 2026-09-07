# without Encapsulation:
# bank - 1000
# Deposit - Money
# Show Balance


# class Bank:
#     def __init__(self):
#         self.balance = 1000

#     def show_balance(self):
#         print(self.balance)

#     def deposit(self, amount):
#         self.balance += amount

# b1 = Bank()

# b1.balance = 0
# # b1.deposit(200)
# b1.show_balance()


# Encapsulation:
# Encapsulation means protecting the data inside a class
# it allows access to data only through class methods, not directly
# it helps keep data safe, controlled, and secure


class Bank:
    def __init__(self):
        self.__balance = 1000   #private

    def show_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

b1 = Bank()
b1.deposit(2000)
b1.__balance = 0
b1.withdraw(200)
b1.deposit(100)
b1.show_balance()