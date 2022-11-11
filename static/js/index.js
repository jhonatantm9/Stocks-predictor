function showElement(){
    var element = document.getElementById("prediction");
    var inputs = [$('#input1').val(), $('#input2').val(), $('#input3').val(),
            $('#input4').val(), $('#input5').val(), $('#input6').val()];
    inputs.forEach(element => {
        if(element == ''){
            return;
        }
    });
    element.style.display = "block";
}

function hideElement(){
    var element = document.getElementById("prediction");
    element.style.display = "none";
    var inputs = [$('#input1'), $('#input2'), $('#input3'),
            $('#input4'), $('#input5'), $('#input6')];
    inputs.forEach(element => {
        element.value = ""
    });

}

