from typing import Callable
from banking_system.utils.exceptions import NegativeAmountError

def validate_transaction(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        amount = kwargs.get('amount') if 'amount' in kwargs else args[1]
        if amount <= 0:
            raise NegativeAmountError()
        return func(*args, **kwargs)
    return wrapper