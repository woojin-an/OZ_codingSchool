from banking_system.utils.exceptions import NegativeAmountError

def validate_transaction(func: callable) -> callable:
    def wrapper(self, amount:int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        return func(self, amount)
    return wrapper