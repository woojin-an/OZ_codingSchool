from services.banking_service import BankingService

def main() -> None:
    while True:
        username = input("당신의 이름을 적어주세요(종료를 원하면 종료를 입력하세요.):")

        if username == "종료":
            break

    banking_service.user_menu(username)

if __name__ == "__main__":
    banking_service = BankingService()

    banking_service.add_user("김코딩")
    banking_service.add_user("박오즈")
    banking_service.add_user("이장고")

    main(banking_service)