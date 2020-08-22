/*  Custom Javascript Functions  */


// Copies to Clipboard 
function copy_to_clipboard(id) {

    var $temp = $("<input>"); 
    $("body").append($temp);
    $temp.val($('#'+id).text()).select();
    document.execCommand("copy");
    $temp.remove();

    // Show Note Was Copied to Clipboard
    toastr.info('Text Has Been Added to Your Clipboard');

}


// Makes Note Favorite 
function make_my_favorite(note_id) {

    $.ajax({
        url: "/make_my_favorite",
        data: {
            "note_id": note_id,
        },
        success: function(result){

            $("#" + note_id + "_fav_button").attr("onclick", "remove_favorite(" + note_id + ");");
            $("#" + note_id + "_fav_button").toggleClass('btn-success btn-danger');
            $("#" + note_id + "_fav_button").html('Dislike');
            $("#" + note_id + "_favorites").html("<i class='far fa-star pr-1'></i>" + (parseInt($("#" + note_id + "_favorites").text()) + 1)); 

        }}, 
    );

}


// Remove Favorite 
function remove_favorite(note_id) {

    $.ajax({
        url: "/remove_favorite",
        data: {
            "note_id": note_id,
        },
        success: function(result){

            $("#" + note_id + "_fav_button").attr("onclick", "make_my_favorite(" + note_id + ");");
            $("#" + note_id + "_fav_button").toggleClass('btn-danger btn-success');
            $("#" + note_id + "_fav_button").html('Like');
            $("#" + note_id + "_favorites").html("<i class='far fa-star pr-1'></i>" + (parseInt($("#" + note_id + "_favorites").text()) - 1));         
        
        }}, 
    );

}