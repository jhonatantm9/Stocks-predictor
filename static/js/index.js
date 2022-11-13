function showElement(){
    var element = document.getElementById("prediction");
    element.style.display = "block";
}

function hideElement(){
    event.preventDefault();
    var element = document.getElementById("prediction");
    element.style.display = "none";
    var inputs = [
        document.getElementById("input1"),
        document.getElementById("input2"),
        document.getElementById("input3"),
        document.getElementById("input4"),
        document.getElementById("input5"),
        document.getElementById("input6")
    ];
    inputs.forEach(inputElement => {
        inputElement.innerHTML == ""
        inputElement.value = "";
    });

}

