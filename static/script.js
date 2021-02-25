async function getQuestion(){
    $.ajax({
        url: "/getQuestion",
        success: function(rs){
           rs.forEach(function(ele){
                 template = `<div style='padding:10px;background-color:#232344;'>
                <div style='width:100%;height:10px;color:white;'>Question ${ele[0].substring(1,2)}: ${ele[1]}</div><br>
                <div style='color:white;'>
                    <form id='answer_option_${ele[0]}'>
                        <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>A. ${ele[2]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>B. ${ele[3]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>C. ${ele[4]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>D. ${ele[5]}</label>
                    </form>
                </div>
            </div>`;
            $("#question_table").append(template);
           })
        },
        dataType: "json"
      });

    return "Success";
}

function hoverSubject(ev){
    // console.log(ev);
    $(ev.currentTarget).css("background-color", "#ff99c2");
}
function subjectMouseOut(ev,color){
    $(ev.currentTarget).css("background-color", color);
}
function loadSubject(){
    $.ajax({
        url: "/getSubject",
        success: function(rs){
            rs.forEach(function(line){
                let color = '#'+Math.floor(Math.random()*16777215).toString(16);
                // let textColor = '#'+Math.floor(Math.random()*16777215).toString(16);
                let template = `<div onmouseover="hoverSubject(event)" onmouseout="subjectMouseOut(event,'${color}')" style="color:black;box-shadow:1px 1px 3px 3px lightblue;text-align:center;display:inline-block;width:80px;height:80px;background-color:${color};"><p>${line[1]}</p></div>`;
                $('#subjects').append(template);
            });
        },
        dataType: "json"
    });



    $('#subjects')
}
function initView(){
    loadSubject();
}