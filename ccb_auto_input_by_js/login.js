setTimeout(function(){

    var username = document.getElementById('USERID');
    username.focus();
    username.value = "leo";
    var password =   document.getElementById('LOGPASS');
    password.focus();
    password.value = "Shine";
    var submitStatic = document.getElementById("J_SubmitStatic");
    submitStatic.focus();
    setTimeout(function(){
        //检测是否需要安全验证
        var noCaptcha = document.getElementById("nocaptcha");
        if(noCaptcha && noCaptcha.className == "nc-container tb-login"
            && noCaptcha.style.display !="block") {
            var submitStatic = document.getElementById("J_SubmitStatic");
            if(submitStatic) submitStatic.click();
        }
    },2000);


},3000);