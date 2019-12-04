#Дескриптор с комиссией
#дескриптор Value, который используется в классе Account
#У аккаунта есть атрибут commission. Именно эта коммиссия вычитается при присваивании значений в amount
class Value:
    def __init__(self, amount = 0):
        self.amount = amount

    def __get__(self, obj, object_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value - value * obj.commission

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

if __name__ == "__main__":
  new_account = Account(0.1)
  new_account.amount = 100

print(new_account.amount)