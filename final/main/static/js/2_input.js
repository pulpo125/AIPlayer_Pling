function enterBtn() {
    // show div
    // const showDiv = document.getElementById("showdiv")
    // showDiv.style.display = 'block'

    let newTitle = $("input[name='new_title']").val();

    // AJAX 요청
    $.ajax({
        url: "similar_ply",
        method: "POST",
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",  // CSRF 토큰 전달
            new_title: newTitle
        },

        success: function (response) {
            var sim_ply_info = response["sim_ply_info"];
            var ply_title = sim_ply_info[1]['ply_title'];

            var newHtml = ''
            for (const info of sim_ply_info) {
                newHtml += '<div id="ply_' + info['ply_id'] + '">'
                    + '<input class="checkbox" type="checkbox" name="select_ply" value="' + info['ply_id'] + '"/>'
                    + '<details>'
                    + '<summary><p class="title">' + info['ply_title'] + '</p></summary>'
                    + '<div class="songbox">';
                for (const meta of info['song_meta']) {
                    newHtml += '<p>' + meta["song_name"] + ' - ' + meta["artist_name"] + '</p>';

                    newHtml += '</div>'
                        + '</details>'
                        + '</div>';
                }
            }

            $("#plyContent").html(newHtml);
        }
    });
}