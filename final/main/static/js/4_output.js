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
}

function captureAndDownload() {
    // 현재 화면만 캡처하고 이미지로 저장
    html2canvas(document.documentElement).then(function (canvas) { // document.documentElement은 현재 화면 전체를 나타냄
        // 이미지 데이터를 URL로 변환
        var image = canvas.toDataURL("image/png");

        // 이미지 다운로드 링크를 생성
        var a = document.createElement("a");
        a.href = image;
        a.download = "screenshot.png"; // 다운로드할 파일 이름 설정
        a.style.display = "none";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
}