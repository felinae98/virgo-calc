$(document).ready(function(){
    $("#enable-pow").parent().click(function(){
        if($("#enable-pow").prop("checked")){
            $("#select-symb").prop("disabled", false);
        }
        else{
            $("#select-symb").prop("disabled", true);
        }
    });
    $("#submit").click(function(){
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
            $("#res-stat").removeClass();
            $("#res-stat").addClass("btn btn-success");
            $("#spinner").hide();
            $("#res-stat").html("生成结果")
        }).fail(function(){
            $("#spinner").hide();
            $("#res-stat").removeClass();
            $("#res-stat").addClass("btn btn-error");
        });
        $("#res-stat").removeClass();
        $("#res-stat").addClass("btn btn-primary");
        $("#spinner").show();
        $("#res-stat").html("加载中");
    });
    var resize_textarea = function(){
        var height = $("footer").offset().top - $("#res-area").offset().top - 30;
        $("#res-area").height(height);
    }
    window.onresize=resize_textarea;
    resize_textarea();
});