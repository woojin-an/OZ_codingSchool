from models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction

class Account:

    bank_name = None
    
    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = []
    
    #입금 메소드
    def deposit(self, amount:int) ->None:

        if amount > 0:
            self.__balance += amount
            self.transaction.append(f"입금: {amount}원")  
            print(f"{amount}원 입금되었습니다. 현재 잔액은 {self.balance}원 입니다.")
        else:
            print("잘못된 입금 금액입니다. 다시 확인해주세요.")

    #출금 메소드
    def withdraw(self, amount:int) ->None:
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.transactions.append(f"출금: {amount}원")
            print(f"{amount}원 출금되었습니다. 현재 잔액은 {self.balance}원 입니다.")
            
        else:
            print("입금 금액이 부족하여 출금할 수 없습니다.")

    #잔고확인 메소드
    def get_balance(self) -> int:
        return self.__balance
    
    #거래내역확인 메소드
    def get_transactions(self) -> list:
        return self.transactions
    

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name