console.log("dbisdvad")
// Obtener elementos
var modal = document.getElementById("miModal");
var btnAbrir = document.getElementById("abrirModal");
var spanCerrar = document.getElementsByClassName("cerrar")[0];

// Al hacer clic en el botón, abre el modal
btnAbrir.onclick = function() {
    modal.style.display = "block";
}

// Al hacer clic en la X, cierra el modal
spanCerrar.onclick = function() {
    modal.style.display = "none";
}

// Al hacer clic fuera del contenido del modal, cierra el modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
