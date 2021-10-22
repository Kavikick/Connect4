function refresh() {
    $.get('/api',function(string) {
        $("#Content").empty()
        $("#Content").append(string)
    })
}
function update(x,y) {
    $.ajax({
        type: "PUT",
        url: "/api",
        data: {x,y}
    })
}