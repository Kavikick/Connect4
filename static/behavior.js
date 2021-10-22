function refresh() {
    $.get('/c4',function(string) {
        $("#Content").empty()
        $("#Content").append(string)
    })
}
function update(x,y) {
    $.ajax({
        type: "PUT",
        url: "/c4",
        data: {x,y}
    })
    refresh();
}
function register(color) {
    $.ajax({
        type: "PUT",
        url: "/register",
        data: {color}
    })
    $('#refresh').css("display","inline")
    refresh()
}
function reset() {
    $.ajax({
        type: "POST",
        url: "/c4"
    })
    $('#reset').remove();
}