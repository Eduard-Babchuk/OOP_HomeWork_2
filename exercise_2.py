import random
import string

class BankAccount:
    def __init__(self, owner_name, initial_balance=0.0):
        self.__account_number = self.__generate_account_number()
        self.__owner_name = owner_name
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, new_name):
        if len(new_name) < 3:
            raise ValueError("Ім'я власника повинно бути не менше 3 символів.")
        self.__owner_name = new_name

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума поповнення повинна бути числом і більшою за 0.")
        self.__balance += amount
        print(f"Поповнення рахунку на {amount} одиниць. Новий баланс: {self.__balance}.")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума зняття повинна бути числом і більшою за 0.")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.__balance -= amount
        print(f"Зняття {amount} одиниць. Новий баланс: {self.__balance}.")

    def __generate_account_number(self):
        return ''.join(random.choices(string.digits, k=10))

    def get_balance(self):
        return self.__balance

    def check_balance(self):
        if self.__balance < 0:
            raise ValueError("Баланс не може бути від'ємним.")
        return self.__balance

try:
    account1 = BankAccount("Іван Петровський", 1000)
    account2 = BankAccount("Марія Коваль", 500)

    print(f"Номер рахунку: {account1.get_account_number()}, Власник: {account1.get_owner_name()}")
    print(f"Номер рахунку: {account2.get_account_number()}, Власник: {account2.get_owner_name()}")

    account1.deposit(200)
    account1.withdraw(150)

    account1.set_owner_name("Іван Сидорович")
    print(f"Нове ім'я власника: {account1.get_owner_name()}")

    print(f"Баланс рахунку 1: {account1.get_balance()}")

    account1.deposit("abc")

except ValueError as e:
    print(f"Помилка: {e}")