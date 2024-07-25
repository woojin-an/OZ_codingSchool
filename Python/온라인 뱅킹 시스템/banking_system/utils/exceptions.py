class InsufficientFundsError(Exception):
    def __init__(self, message: str = "Insufficient funds for the transaction."):
        super().__init__(message)           # super: 부모 호출

class NegativeAmountError(Exception):
    def __init__(self, message: str = "Amount must be greater than zero."):
        super().__init__(message)

class UserNotFoundError(Exception):
    def __init__(self, message: str = "User not found."):
        super().__init__(message)