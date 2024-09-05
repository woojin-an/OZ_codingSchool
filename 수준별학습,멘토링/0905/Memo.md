함수 입장에서 받는것은 매개변수(파라미터)
외부로부터 주는 것은 인자 (argument)

### debug
* evaluate expression 대신에 스레드&배리어블 평면에 우클릭 -> watch 에 입력해도 확인 가능함
* httpie 를 활용하여 직접 브라우저에 접속하지 않고도, 요청으로 인한 어떤 응답이 돌아오는지 확인 가능
* 사용법 | (설치: `brew install httpie`), (명령어: `http #주소#`)

### Unit Test
* TestCase 상속하여 유닛 테스트 하는 법
* assert 이용하기 (True 일 경우 테스트 통과, False일 경우 assertion error)
* 배포 가능한지 불가능한지 여부를 가리기 위해 유닛테스트 ***필수로*** 진행하여야 함