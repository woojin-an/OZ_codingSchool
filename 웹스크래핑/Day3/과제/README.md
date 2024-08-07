### 네트워크 7계층 (OSI 7 layers)

우선 네트워크 7계층은 다음과 같다. 
1. 물리 계층 (Physical Layer)
2. 데이터 링크 계층 (Data Link Layer)
3. 네트워크 계층 (Network Layer)
4. 전송 계층 (Transport Layer)
5. 세션 계층 (Session Layer)
6. 표현 계층 (Presentation Layer)
7. 응용 계층 (Application Layer)

각 계층에 대한 간략한 설명은 다음과 같다.

---
> 1. 물리 계층 (Physical Layer)
> 
우선 데이터를 주고 받기 위해서는 데이터를 물리적인 신호로 주고 받아야 하므로 데이터를 물리적인 신호로 변환되어 전송되는 계층
> 2. 데이터 링크 계층 (Data Link Layer)
> 
물리 계층에서 받은 신호를 MAC 주소를 통해 네트워크 내에서 장치간의 통신을 하게 됨

> 3. 네트워크 계층 (Network Layer)
> 
IP 주소를 이용하여 목적지까지 데이터가 이동함. 이때 로컬뿐 아니라 다른 네트워크로도 이동함.

> 4. 전송 계층 (Transport Layer)
> 
데이터 전송의 신뢰성을 보장하며, 전송이 되었는지를 확인함

> 5. 세션 계층 (Session Layer)
> 
두 장치간의 세션이 설정되고 관리됨.

> 6. 표현 계층 (Presentation Layer)
> 
데이터의 표현 방식(ex. 암호화, 압축 등)을 처리하며, 데이터 형식 간 변환을 담당함

> 7. 응용 계층 (Application Layer)
> 
사용자가 직접 상호작용 하는 계층으로, 웹브라우저 또는 애플리케이션 등을 말함

---

그렇다면 주소창에 naver.com 을 입력하였을 때 네트워크 7계층에서 일어나는 일은 무엇일까?
아주 간단히 요약해보자면 다음과 같다.

**7단계 응용계층**에서는 웹브라우저에 naver.com을 입력하고, 브라우저는 naver.com의 IP주소를 찾음  
이후 HTTP(S)요청을 통해 해당 웹 서버에서 웹 페이지 데이터를 요청하고, 브라우저는 해당 데이터를 표시하여 줌

**6단계 표현계층**에서는 웹 브라우저가 서버로부터 받은 데이터를 사용자에게 보여주기 위한 형식으로 변환함.
예를 들면 HTML, CSS, JavaScript 파일 등이 웹 브라우저에서 해석되어 화면에 표시됨

**5단계 세션계층**에서는 웹 브라우저와 naver.com 서버 간의 세션이 관리됨.

**4단계 전송계층**에서는 TCP 또는 UDP 프로토콜을 사용하여 데이터가 올바르게 전송되는지 확인함.  

**3단계 네트워크 계층**에서는 naver.com 서버로 데이터를 보내기 위한 경로를 결정함

**2단계 데이터 링크 계층**에서는 로컬 네트워크 내 라우터 또는 스위치로 데이터를 전달함

**1단계 물리 계층**에서는 위에서 처리된 데이터들이 물리적 신호로 전달됨

---

각 계층에서 좀 더 세부적으로 살펴볼 개념들은 다음과 같다.

> HTTP(S) - Application Layer
> 
HTTP는 웹 브라우저와 웹 서버 간의 통신을 위해 개발되었으며, HTML, CSS, Javascript 등의 문서를 전송하기 위한 표준 프로토콜로 사용됨  
이는 plain text로 전송되기 때문에 보안에 취약하므로 보안성이 높은 HTTPS가 등장함  
HTTPS의 동작 방식은 SSL/TLS 암호화 방식을 사용하여 인증 요청을 보내고 인증서를 신뢰할 수 있는가를 확인하여 클라이언트-서버 간의 비밀키를 사용해 데이터를 암호화 하고 전송함

> TCP / UDP 프로토콜 - Transport Layer
> 
보통 TCP 프로토콜을 사용하는데, 이는 데이터가 제대로 도착했는지 일일이 확인하여 도착하지 않았다면 재요청을 하는 등 신뢰성이 뛰어남.
UDP 프로토콜은 신뢰성보단 속도가 중요하므로 스트리밍, 음성통화 등에 사용됨

> MAC Address - Data Link Layer
> 
동일 또는 다른 네트워크 상에 있는 장치들이 서로를 인식하기 위해 갖고있는 고유의 주소  
앞 6자리는 생산자를 나타내는 코드이고, 뒤 6자리는 장비 고유의 번호임

> 공인/사설 IP - Network Layer
> 
공인 IP는 전세계적으로 ICANN이라는 기관에서 국가별 공인 IP를 관리하며, 우리나라에서는 한국인터넷진흥원에서 관리함  
이것을 ISP(통신사)가 부여받아 고객들에게 제공함

사설 IP는 통신사로부터 제공받는 IP로 인터넷 환경을 이용할 때 공유기를 사용한다면 해당 공유기(로컬네트워크)에서는 내부적으로 사용되는 고유한 주소임

> ARP - Data Link Layer
>
ARP는 주소 결정 프로토콜으로, IP주소와 MAC주소를 연결지어 데이터가 올바른 주소로 이동하게끔 해주는 프로토콜임  
장비들이 스위치로 연결된 네트워크에는 ARP table이 존재하여 MAC주소를 추적할 수 있음
