document.addEventListener('readystatechange', function() {
    if (document.readyState === "complete") {
      console.log("Connected !!")
      init();
    }
});

function init(){
    var td_fields = document.querySelectorAll('td');
    for(var i= 0; i < td_fields.length; i++){
        td_fields[i].addEventListener('click', markerManager)
    }

    var restart_btn = document.getElementById('restart_btn');
    restart_btn.addEventListener('click', clearBoard)

}

function markerManager(){
    if(this.textContent === ''){
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent = 'O';
    }else{
        this.textContent = '';
    }
}

function clearBoard(){
    var td_fields = document.querySelectorAll('td');
    for(var i= 0; i < td_fields.length; i++){
        td_fields[i].textContent = '';
    }
}