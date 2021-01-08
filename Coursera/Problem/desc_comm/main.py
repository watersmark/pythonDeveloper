class Value:

    def __init__(self, amount=0):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value * (1 - obj.commission)

# class Account:
#     amount = Value()
#
#     def __init__(self, commission):
#         self.commission = commission
#
#
# new_account = Account(0.1)
# new_account.amount = 100
#
# print(new_account.amount)