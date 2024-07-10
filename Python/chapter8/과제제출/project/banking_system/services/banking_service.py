from models.user import User
from banking_system.models.user import User
from utils.exceptions import UserNotFoundError

class Banking_service:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, username: str) -> None:
        new_user = User(username)
        self.users.append(new_user)

    def find_user(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(f"{username}을 찾을 수 없습니다.")
    
    def user_menu(self, username: str) -> None:
        try:
            user = self.find_user(username)
        except UserNotFoundError as e:
            print(e)
            return
        
        while True:
            mode = input("원하는 기능을 입력하세요[입금, 출금, 잔고확인, 거래내역, 종료]: ")

            if mode == "입금":
                amount = int(input("입금 금액을 숫자만 입력하세요: "))
                user.account.deposit(amount)
            
            elif mode == "출금":
                amount = int(input("출금 금액을 숫자만 입력하세요: "))
                user.account.withdraw(amount)

            elif mode == "잔고확인":
                user.account.get_balance()

            elif mode == "거래내역":
                user.account.get_transaction()

            elif mode == "종료":
                break

            else:
                print("잘못 입력하셨습니다. 다시 확인 후 입력해주세요.")