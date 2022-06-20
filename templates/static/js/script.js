function preview_1() {
    image_1.src=URL.createObjectURL(event.target.files[0]);
}

function preview_2() {
    image_2.src=URL.createObjectURL(event.target.files[0]);
}

function preview_3() {
    image_3.src=URL.createObjectURL(event.target.files[0]);
}

function remove(id) {
    let x = document.getElementById('remove${this}').value;
    console.log(x)
    let question = confirm("Deseja remover seu anúncio?") 
    if(question == true){
        window.location.href = x
    }
}
