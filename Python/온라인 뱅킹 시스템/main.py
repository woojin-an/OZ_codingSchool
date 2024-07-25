from banking_system.services.banking_service import BankingService

def main() -> None:
    system = BankingService()           #유저 넣는 리스트 / 유저 추가 기능 / 유저 찾는 기능 / 입금 / 출금
    
    while True:
        mode = input("1. 사용자 추가 2. 사용자 찾기 3. 거래기능 4. 종료:")

        if mode == '1':
            username = input("추가할 사용자 이름을 입력하세요: ")
            system.add_user(username)
        
        elif mode == '2':
            username = input("찾을 사용자 이름을 입력하세요: ")
            system.find_user(username)

        elif mode == '3':
            username = input("거래할 사용자 이름을 입력하세요.: ")
            system.user_menu(username)

        elif mode == '4':
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()

