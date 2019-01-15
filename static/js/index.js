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
    $("#start-button").click(function(){
        $.ajax({
            url: "/start",
            type: "POST",
            data: {
                num: $("#start-num").prop("value"),
                enable_frac: $("#start-frac").prop("checked"),
                enable_pow: $("#start-pow").prop("checked")
            }
        }).done(function(data){
            $("#start-div").hide();
            $("#prob-div").show();
            res = JSON.parse(data);
            $("#prob-text").html(res.porb);
            $("#cur-prob-num").html(res.cur_num);
            $("#all-prob-num").html(res.all_num);
        })
    });
    $("#submit-ans").click(function(){
        $.ajax({
            url: "/submit",
            type: "POST",
            data: {
                ans: $("#ans").prop("value")
            }
        }).done(function(data){
            res = JSON.parse(data);
            if(res.correct){
                $("#ans-correct").show();
            }
            else{
                $("#ans-error").show();
                $("#correct-value").html(res.ans);
            }
        })
    });
    $("#next-prob").click(function(){
        $("#ans-correct").hide();
        $("#ans-error").hide();
        $("#ans-error").prop("value", "");
        $.ajax({
            url: "/next",
            type: "POST",
        }).done(function(data){
            res = JSON.parse(data);
            $("#prob-text").html(res.prob);
            $("#cur-prob-num").html(res.cur_num);
            $("#all-prob-num").html(res.all_num);
        })
    })
});