async function getQuestion(){
    // var xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange=function() {
    // if (this.readyState == 4 && this.status == 200) {
    //     rs = this.response;
    //     rs_arr = rs.split("-");
    //     rs_arr.forEach(function(item){
    //         answer = ["answer A","answer B","answer C", "answer D"];
    //         template = `<div style='padding:10px;background-color:#232344;'>
    //             <div style='width:100%;height:100px;color:white;'>${item}<br>
    //             <input type='radio' name='an_A' value='answerA'><label for='an_A'>${answer[0]}</label>
    //             <input type='radio' name='an_B' value='answerB'><label for='an_B'>${answer[1]}</label>
    //             <input type='radio' name='an_C' value='answerC'><label for='an_C'>${answer[2]}</label>
    //             <input type='radio' name='an_D' value='answerD'><label for='an_D'>${answer[3]}</label>
    //         </div>`;
    //         $("#question_table").append(template);
    //     });
        
    //     $("#question_table").append("<button>Submit</button>");
    // }
    // };
    // xhttp.open("GET", "/getQuestion", true);
    // xhttp.send();

    $.ajax({
        url: "/getQuestion",
        success: function(rs){
           rs.forEach(function(ele){
                 template = `<div style='padding:10px;background-color:#232344;'>
                <div style='width:100%;height:10px;color:white;'>Question ${ele[0].substring(1,2)}: ${ele[1]}</div><br>
                <div style='color:white;'>
                <input type='radio' name='an_A' value='answerA'><label for='an_A'>A. ${ele[2]}</label>
                <input type='radio' name='an_B' value='answerB'><label for='an_B'>B. ${ele[3]}</label>
                <input type='radio' name='an_C' value='answerC'><label for='an_C'>C. ${ele[4]}</label>
                <input type='radio' name='an_D' value='answerD'><label for='an_D'>D. ${ele[5]}</label>
                </div>
            </div>`;
            $("#question_table").append(template);
           })
        },
        dataType: "json"
      });

    return "Success";
}