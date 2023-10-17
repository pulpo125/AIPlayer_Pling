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

// 추천 결과 생성 중
const generateRec = () => {
    return new Promise((resolve, reject) => {
        console.log(selectPlyList);
        console.log("js generateRec start");
        $.ajax({
            url: "recAI",
            method: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: "{{ csrf_token }}",
                select_ply_lst: selectPlyList,
                similarity: similarity,
                song_num: songNum
            },

            beforeSend: function () {
                console.log("start generateRec");
                setTimeout(loadingRec, 2000);
            },
    
            success: function (response) {
                console.log("success generateRec");
                setTimeout(endRec, 2000);
                resolve();
            },

            error: function (err) {
                reject(err);
            }
        });
    });
}
// 추천 결과 생성 완료

// 이미지 생성 중
const generateImg = () => {
    return new Promise((resolve, reject) => {
	    console.log("js generateImg start");
        $.ajax({
            url: "imageAI",
            method: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },

            beforeSend: function () {
                console.log("start generateImg");
                setTimeout(loadingImg, 2000);
            },
    
            success: function (response) {
                console.log("success generateImg");
                resolve(response);
            },

            error: function (err) {
                reject(err.error);
            }
        });
    });
}
// 이미지 생성 완료

async function run() { 
   try {
       await generateRec();
       await generateImg(); 
   } catch (err) {
   }
   endImg();
   redirectToOutput();
};

run();

