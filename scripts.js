function $(q){
    return document.querySelectorAll(q)
}
$("embed").forEach(function(t){
    t.height = window.innerHeight
    t.width = window.innerWidth
})