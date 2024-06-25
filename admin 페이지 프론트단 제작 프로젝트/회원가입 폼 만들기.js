const form = document.getElementById("form")


form.addEventListener("submit", function(event){
  event.preventDefault() // 기존 기능 차단(제출 시 리셋되던 기능)

  let userId = event.target.id.value
  let userPw1 = event.target.pw1.value
  let userPw2 = event.target.pw2.value
  let userName = event.target.name.value
  let userPhone = event.target.phone.value
  let userPosition = event.target.position.value
  let userGender = event.target.gender.value
  let userEmail = event.target.email.value
  let userIntro = event.target.intro.value
  

  console.log(userId, userPw1, userPw2, userName, 
    userPosition, userGender, userEmail, userIntro)

  if(userId.length < 6){
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
    return  //함수 강제종료함
  }
  if(userPw1 !== userPw2){
    alert("비밀번호가 일치하지 않습니다.")
    return
  }

  //가입 잘 되었다 환영
  document.body.innerHTML = ""
  document.write(`
    <p>
    ${userName}님 환영합니다! <br>
    회원 가입 시 입력하신 내역은 다음과 같습니다.<br><br>
    아이디 : ${userId}<br>
    이름 : ${userName}<br>
    전화번호 : ${userPhone}<br>
    원하는 직무 : ${userPosition}<br>
    </p>
    `)

})