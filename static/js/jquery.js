$(document).ready(function(){
    console.log("Hello");

    function ajax_formulario(){
        $.ajax({
            url:"/respuesta",
            data: $('form').serialize(),
            type:'POST',
            success:function(response)
            {
                alert('success');
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        })
    }

    $('formulario').on(function(event){
        console.log("Click");
        event.preventDefault();
        ajax_formulario();
    })
});


/*$(document).on('submit','#formulario',function(e)
				{
                console.log('hello');
                e.preventDefault();
                $.ajax({
                    type:'POST',
                    url:"/",
                    data:{
                    'OpIn_Over_NWC_FA':$("#input1").val(),
                    'OpIn_Over_InterestExpense':$("#input2").val(),
                    'WorkingCapitalRatio':$("#input3").val(),
                    'RoE':$("#input4").val(),
                    'Asset_Turnover':$("#input5").val(),
                    'Gross_Profit_Margin':$("#input6").val()
                    },
                    success:function()
                    {
                    alert('success');
                    }
                })
                });*/