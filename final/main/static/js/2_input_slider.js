var slider1 = document.getElementById("mySlider1");
var sliderValueDisplay1 = document.getElementById("sliderValueDisplay1");

var slider2 = document.getElementById("mySlider2");
var sliderValueDisplay2 = document.getElementById("sliderValueDisplay2");

const imageContainer = document.querySelector('.image-container');
const hoverImage = document.querySelector('.hover-image');

imageContainer.addEventListener('mouseenter', () => {
    hoverImage.style.opacity = '1'; // mousehover시 이미지가 나타남
});

imageContainer.addEventListener('mouseleave', () => {
    hoverImage.style.opacity = '0'; // 호버가 끝나면 이미지가 숨겨짐
});
slider1.oninput = function() {
    var sliderValue1 = this.value;
    sliderValueDisplay1.innerText = sliderValue1;
    // 슬라이더1 값이 변경될 때 호출할 작업을 여기에 추가
    // 슬라이더1 값이 변경될 때마다 콘솔에 로그 출력
    console.log("슬라이더 1 값이 변경됨:", sliderValue1);
}

slider2.oninput = function() {
    var sliderValue2 = this.value;
    sliderValueDisplay2.innerText = sliderValue2;
    // 슬라이더2 값이 변경될 때 호출할 작업을 여기에 추가
    // 슬라이더2 값이 변경될 때마다 콘솔에 로그 출력
    console.log("슬라이더 2 값이 변경됨:", sliderValue2);
}

// 버튼 위치를 변경하는 함수
function updateSliderPosition1(newPosition) {
    slider1.value = newPosition;
    sliderValueDisplay1.innerText = newPosition;
}

function updateSliderPosition2(newPosition) {
    slider2.value = newPosition;
    sliderValueDisplay2.innerText = newPosition;
}

function updateValue() {
    // 슬라이드바 값이 변경될 때 호출할 작업을 여기에 추가
    // 슬라이드바 값이 변경될 때마다 콘솔에 로그 출력
    console.log("슬라이드바 값이 변경됨:", slider1.value, slider2.value);
}


