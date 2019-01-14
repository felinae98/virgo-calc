$(document).ready(function(){
    $("#enable-pow").parent().click(function(){
        if($("#enable-pow").prop("checked")){
            $("#select-symb").prop("disabled", false);
        }
        else{
            $("#select-symb").prop("disabled", true);
        }
    });
    $("#generate").click(function(){
        $.ajax({
            url: "/generate",
            type: "POST",
            data: {
                num: $("#prob-num").prop("value"),
                enable_frac: $("#enable-frac").prop("checked"),
                show_ans: $("#enable-ans").prop("checked"),
                enable_pow: $("#enable-pow").prop("checked"),
                pow_symb: $("#select-symb").prop("value")
            }
        }).done(function(data){
            $("#res-area").html(data);
        })
    });
});