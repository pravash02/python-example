document.addEventListener('readystatechange', function() {
    if (document.readyState === "complete") {
      console.log("Connected !!")
      init();
    }
});

function init(){
      var player1 = prompt("Enter your name. your color will be blue");
      var player1Color = 'rgb(86, 151, 255)';
      var player2 = prompt("Enter your name. your color will be red");
      var player2Color = 'rgb(237, 45, 73)';

      var game_on = true;
      var table = $('table tr');

      var currentPlayer = 1;
      var currentName = player1;
      var currentColor = player1Color;

      $('h1').text(player1 + " it is your turn")

      $('.board button').on('click', function(){
        var col = $(this).closest('td').index();
        var bottomAvail = checkBottom(col);
        changeColour(bottomAvail, col, currentColor)

        if (horizontalWin() || verticalWin()){
            $('h1').text(currentName + ' Won !!');
            $('p').text('Refresh to start new game');
        }else{
            currentPlayer = currentPlayer * -1;
            if (currentPlayer === 1){
                currentName = player1;
                $('h1').text(currentName + " it is your turn")
                currentColor = player1Color;
            }else {
                currentName = player2;
                $('h1').text(currentName + " it is your turn")
                currentColor = player2Color;
            }
        }
      })
}

function changeColour(rowIndex, colIndex, color){
    var table = $('table tr');
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function checkColour(rowIndex, colIndex){
    var table = $('table tr');
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex){
    var colorReport = checkColour(5, colIndex);
    for(row = 5; row > -1; row --){
        colorReport = checkColour(row, colIndex)
        if (colorReport === 'rgb(128, 128, 128)'){
            return row
        }
    }
}

function colourMatchCheck(one, two, three, four){
    return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== 'undefined')
}

function horizontalWin(){
    for (var row =0; row < 6; row++){
        for (var col =0; col < 4; col++){
            if (colourMatchCheck(checkColour(row, col), checkColour(row, col+1), checkColour(row, col+2), checkColour(row, col+3))) {
                console.log('horizontal');
                console.log('Win !!');
                return true;
            }else{
                continue;
            }
        }
    }
}

function verticalWin(){
    for (var col =0; col < 7; col++){
        for (var row =0; row < 3; row++){
            if (colourMatchCheck(checkColour(row, col), checkColour(row+1, col), checkColour(row+2, col), checkColour(row+3, col))) {
                console.log('vertical');
                console.log('Win !!');
                return true;
            }else{
                continue;
            }
        }
    }
}