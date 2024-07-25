from banking_system.models.user import User
from banking_system.utils.exceptions import UserNotFoundError

class BankingService:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, username: str) -> None: # 유저 추가가 먼저 되어야 기능이 돌아가므로
        self.users.append(User(username))

    def find_user(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(f"{username}을 찾을 수 없습니다.")
    
    def user_menu(self, username:str) -> None:
        user = self.find_user(username)

        while True:
            try:
                mode = input("원하는 기능을 입력하세요[1.입금, 2.출금, 3.잔고확인, 4.거래내역, 5.초기화면]: ")
                
                #입금
                if mode == "1":
                    amount = int(input("입금 금액을 숫자만 입력하세요: "))
                    user.account.deposit(amount)
                
                #출금
                elif mode == "2":
                    amount = int(input("출금 금액을 숫자만 입력하세요: "))
                    user.account.withdraw(amount)

                #잔고확인
                elif mode == "3":
                    print(f"잔고: {user.account.get_balance()}원")

                #거래내역
                elif mode == "4":
                    for transaction in user.account.get_transactions():
                        print(transaction)

                #종료
                elif mode == "5":
                    print("초기화면으로 돌아갑니다.")
                    break
                
                else:
                    print("잘못된 입력입니다. 다시 확인해주세요.")

            except ValueError as e:
                print(f"잘못된 입력입니다.")
            