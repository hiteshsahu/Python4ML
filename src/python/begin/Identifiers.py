"""
Variable Declearation :

-  Contain only (A-z, 0-9, and _ )
-  Start with a lowercase letter or _.
-  Single leading _* :  private
-  Double leading __* :  strong private
-  Start & End  __*__ : Language defined Special Name
-  CASE SENSITIVE
-  Class names start with an uppercase letter.
-

"""


class BankAccount(object):

    def __init__(self, name, money, password):
        self.name = name            # Public
        self._money = money         # Private : Package Level
        self.__password = password  # Super Private

    def earn_money(self, amount):
        self._money += amount
        print("Salary Received: ", amount, " Updated Balance is: ", self._money)

    def withdraw_money(self, amount):
        self._money -= amount
        print("Money Withdraw: ", amount, " Updated Balance is: ", self._money)

    def show_balance(self):
        print(" Current Balance is: ", self._money)


account = BankAccount("Hitesh", 1000, "PWD")  # Object Initalization

# Method Call
account.earn_money(100)

# Show Balance
print(account.show_balance())

print("PUBLIC ACCESS:", account.name)  # Public Access

# account._money is accessible because it is only hidden by convention
print("PROTECTED ACCESS:", account._money)  # Protected Access

# account.__password will throw error but account._BankAccount__password will not
# because __password is super private
print("PRIVATE ACCESS:", account._BankAccount__password)

# Method Call
account.withdraw_money(200)

# Show Balance
print(account.show_balance())

# account._money is accessible because it is only hidden by convention
print(account._money)  # Protected Access