function startMoving(){
    var progress = document.getElementById("progress");
    var width = 0;
    var id = setInterval(frame, 10000);
    document.getElementById("btn-tac-request").style.display = "none"
    progress.style.backgroundColor = "#3e70ef"
    function frame(){
        if (width == 100){
            clearInterval(id);
            document.getElementById("another-tac-request").classList.remove("hide");
        }else{
            width++;
            if(width > 50 && width < 70 ){
                progress.style.backgroundColor = "#efbf3e";
            }else if(width > 70){
                progress.style.backgroundColor = "red";
            }
            progress.style.width = width + '%';
        }
    }
}

function showForm(){
    document.getElementById("tac-form").classList.remove("hide-tac-form");
    document.getElementById("tac-form").classList.add("show-tac-form");
    document.getElementById("another-tac-request").classList.add("hide")
}

function growActivate(){
    document.querySelector("h1.activated").classList.add("bigger");
    document.getElementById("headsup").style.opacity = "1";
    document.getElementById("headsup").style.color = "white";
    document.getElementById("headsup").style.transition = "ease-in 550ms";
}
