function downloadImage() {
    // 이미지 파일 URL 설정 
    var imageUrl = '/static/result/pubao.jpg';  

    // 새로운 <a> 요소를 동적으로 생성하여 이미지 다운로드 링크 생성
    var a = document.createElement('a');
    a.href = imageUrl;  // 이미지 파일 URL을 링크의 href 속성에 설정
    a.download = 'pubao.jpg';  // 다운로드할 파일 이름 설정
    a.style.display = 'none';  // 화면에 표시하지 않도록 설정

    // <a> 요소를 body에 추가하여 클릭 이벤트를 발생
    document.body.appendChild(a);
    a.click();

    // <a> 요소를 삭제
    document.body.removeChild(a);

    // 데이터 URL 출력 (확인용)
    console.log('Data URL:', imageUrl);
}
function captureAndDownload() {
    // 현재 화면 전체를 캡처하기 위해 document.body를 대상으로 설정
    html2canvas(document.body, {
        scrollX: 0, // 가로 스크롤을 없애기 위해 0으로 설정
        scrollY: 0, // 세로 스크롤을 없애기 위해 0으로 설정
        windowWidth: document.documentElement.offsetWidth, // 화면 너비 설정
        windowHeight: document.documentElement.offsetHeight, // 화면 높이 설정
    }).then(function (canvas) {
        // 이미지 데이터를 URL로 변환
        var image = canvas.toDataURL("image/png");

        // 이미지 다운로드 링크를 생성
        var a = document.createElement("a");
        a.href = image;
        a.download = "screenshot.png"; // 다운로드할 파일 이름 설정
        a.style.display = "none";
        document.body.appendChild(a);

        // 이미지 다운로드 링크를 클릭
        a.click();

        // 다운로드를 위해 생성한 요소를 제거
        document.body.removeChild(a);
    });
}