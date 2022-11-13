$("#resultado").click(function(){
    $.ajax({
        url : "register_email_newslatter/",
        type : 'post',
        data : {
            'email': $("#email").val()
        },
        beforeSend : function(){
            $("#resultado").html("Enviando...");
        }
    })
    .done(function(msg){
        alert(msg);
        $("#resultado").html("Assinar");
    })
    .fail(function(jqXHR, textStatus, msg){
        alert(msg);
    });
});