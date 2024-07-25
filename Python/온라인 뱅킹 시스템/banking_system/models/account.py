from banking_system.models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError

class Account:
    bank_name = "Mybank"
    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name

    def __init__(self) -> None:
        self.__balance = 0      # 계좌에 들어가는 초기 금액
        self.transactions = []  # 거래내역
    
    @validate_transaction            # 데코레이터 먼저 실행 후 함수 진행
    def deposit(self, amount:int) ->None:
        # if amount <= 0:             # 음수일때 error
        #     raise NegativeAmountError()
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))

    @validate_transaction            # 데코레이터 먼저 실행 후 함수 진행
    def withdraw(self, amount:int) ->None:
        # if amount <= 0:             # 음수일때 error
        #     raise NegativeAmountError()
        
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
    
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        return self.__balance
    
    def get_transactions(self) -> list:
        return self.transactions
    
    