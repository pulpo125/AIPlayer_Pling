// // 데이터가 DB에 저장되면 자동으로 다음 페이지로 이동
// function redirectToOutput() {
//     // 페이지 리디렉션
//     window.location.href = "{% url 'output' %}";
// }

// // 페이지 로딩이 완료되면 redirectToOutput 함수를 호출하여 리디렉션 수행
// window.onload = redirectToOutput;
const RecLoad = document.getElementById("RecLoad")
const RecEnd = document.getElementById("RecEnd")
const ImgLoad = document.getElementById("ImgLoad")
const ImgEnd = document.getElementById("ImgEnd")

function loadingRec() {
    RecLoad.style.display = "block";
}

function endRec() {
    RecLoad.style.display = "none";
    RecEnd.style.display = "block";
}

function loadingImg() {
    ImgLoad.style.display = "block";
}

function endImg() {
    ImgLoad.style.display = "none";
    ImgEnd.style.display = "block";
}

setTimeout(loadingRec, 2000); // 2초 후 실행
setTimeout(endRec, 7000); 
setTimeout(loadingImg, 9000); // 17 초 후 실행 
setTimeout(endImg, 19000); 
