$(document).ready(function(){


});

function submitContactUs(){
    var name = $("#name").val();
    var email = $("#email").val();
    var message = $("#message").val();

    var regEmail = /^([A-Za-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;

    if( name == '' || name.length>16 ){
        //$("#name").css("borderColor","red");
        $("#name").val("");
        $("#name").focus();
        return;
    }
    if( email == '' || !regEmail.test(email) ){
        //$("#email").css("borderColor","red");
        $("#email").val("");
        $("#email").focus();
        return;
    }
    if( message == '' ){
        //$("#message").css("borderColor","red");
        $("#message").val("");
        $("#message").focus();
        return;
    }
    $("#submitBtn").click();
    //成功提交后增加disabled属性，防止多次提交
    $("#submitBtn").attr("disabled","disabled")
}