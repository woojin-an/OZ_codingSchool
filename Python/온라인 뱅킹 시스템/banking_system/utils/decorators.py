from banking_system.utils.exceptions import NegativeAmountError
from typing import Callable
def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount:int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        return func(self, amount)
    return wrapper