// script.js
// 다크모드
document.getElementById('darkModeToggle').addEventListener('click', function() {
  document.body.classList.toggle('dark-mode');
  
  // 버튼 텍스트 업데이트
  if (document.body.classList.contains('dark-mode')) {
      this.textContent = '다크모드 해제'
  } else {
      this.textContent = '다크모드';
  }
});

// 현재 날짜와 시간을 표시하는 함수
function updateClock() {
  const now = new Date();
  const year = now.getFullYear().toString().padStart(2, '0');
  const month = (now.getMonth() + 1).toString().padStart(2, '0');
  const date = now.getDate().toString().padStart(2, '0');
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  
  const formattedTime = 
  `${year}년 ${month}월 ${date}일 ${hours}:${minutes}:${seconds}`;
  
  document.getElementById('clock').textContent = formattedTime;
}

// 페이지 로드 시 시계를 즉시 업데이트하고 매초마다 업데이트
updateClock();
setInterval(updateClock, 1000);


//회원가입 버튼 클릭 시 이동
document.getElementById('signup').onclick = function() {
  window.open('회원가입 폼 만들기.html', '_blank')
};

