function like(pk) {
    var element = document.getElementById('like')
    $.get("/product/like/" + pk).then(response =>{
        if (response['response'] === 'liked'){
            element.className = 'hover:text-green-600'
        }else {
            element.className = '#heart'
        }
    })
    
}