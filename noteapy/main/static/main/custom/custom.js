function copy_to_clipboard(id) {

    var $temp = $("<input>"); 
    $("body").append($temp);
    $temp.val($('#'+id).text()).select();
    document.execCommand("copy");
    $temp.remove();

}