$(document).ready(function(){
    $.ajax({
        type : "GET",
        url : get_url,
        success : function(data){
            console.log(data);
        }
    });
})