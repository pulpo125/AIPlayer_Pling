// 썸네일 이미지 다운로드 
function downloadImage() {
    var imageUrl = '/static/result/result_img.png';  

    var a = document.createElement('a');
    a.href = imageUrl;  // 이미지 파일 URL을 링크의 href 속성에 설정
    a.download = 'result_img.png';  // 다운로드할 파일 이름 설정
    a.style.display = 'none';  // 화면에 표시하지 않도록 설정

    document.body.appendChild(a);
    a.click();

    document.body.removeChild(a);
}

// 화면 캡처 다운로드
function captureAndDownload() {
    
    html2canvas(document.body, {
        scrollX: 0, // 가로 스크롤을 없애기 위해 0으로 설정
        scrollY: 0, // 세로 스크롤을 없애기 위해 0으로 설정
        windowWidth: document.documentElement.offsetWidth, // 화면 너비 설정
        windowHeight: document.documentElement.offsetHeight, // 화면 높이 설정
    }).then(function (canvas) {
        
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


//  좋아요 버튼 클릭 시
function likePlaylist() {

    $.ajax({
        url: "like_ply",
        method: "POST",
        dataType: "json", 
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}"
        },
        success: function (data) {
            if (data.success) {
                alert("좋아요가 반영 되었습니다!");
            } else {
                alert("좋아요를 반영 중 오류가 발생했습니다.");
            }
        },
        error: function() {
            // 요청이 실패한 경우 실행할 코드
            alert("서버와 통신 중 오류가 발생했습니다.");
        }
    });

    $('#likeForm').submit();
}


//  좋아요 버튼 마우스 오버
const likeBtn = document.querySelector('#likeBtn');
const likeHover = document.querySelector('#likeHover');

likeBtn.addEventListener('mouseenter', () => {
    likeHover.style.opacity = '1'; // mousehover시 이미지가 나타남
});

likeBtn.addEventListener('mouseleave', () => {
    likeHover.style.opacity = '0'; // 호버가 끝나면 이미지가 숨겨짐
});

//  썸네일 이미지 다운로드 버튼 마우스 오버
const dwBtn = document.querySelector('#dwBtn');
const dwHover = document.querySelector('#dwHover');

dwBtn.addEventListener('mouseenter', () => {
    dwHover.style.opacity = '1'; // mousehover시 이미지가 나타남
});

dwBtn.addEventListener('mouseleave', () => {
    dwHover.style.opacity = '0'; // 호버가 끝나면 이미지가 숨겨짐
});

//  캡처 버튼 마우스 오버
const capBtn = document.querySelector('#capBtn');
const capHover = document.querySelector('#capHover');

capBtn.addEventListener('mouseenter', () => {
    capHover.style.opacity = '1'; // mousehover시 이미지가 나타남
});

capBtn.addEventListener('mouseleave', () => {
    capHover.style.opacity = '0'; // 호버가 끝나면 이미지가 숨겨짐
});