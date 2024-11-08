document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.getAttribute('data-post-id');

        fetch('{% url "like_post" %}', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ post_id: postId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const likeCount = this.nextElementSibling;
                likeCount.textContent = `${data.likes} likes`; // Actualiza el conteo de likes
            } else {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});


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

document.addEventListener("DOMContentLoaded", function() {
    let grupoSeleccionado = null; // Variable para almacenar el área seleccionada
    let nombreSeleccionado = null; // Variable para almacenar el nombre del área seleccionada
    const inputAreasSeleccionadas = document.getElementById('grupoSeleccionado');

    // Seleccionar todos los elementos de las áreas de interés (cargadas desde el servidor)
    const areaItems = document.querySelectorAll('#groupsInteresList li');

    // Añadir event listeners a cada área de interés en la lista
    areaItems.forEach(area => {
        area.addEventListener('click', function() {
            const areaId = this.getAttribute('data-id');
            const areaNombre = this.getAttribute('data-nombre');

            // Si ya hay un área seleccionada, la deseleccionamos
            if (grupoSeleccionado !== null) {
                document.querySelector(`[data-id="${grupoSeleccionado}"]`).classList.remove('selected');
            }

            // Seleccionamos la nueva área (o deseleccionamos si ya estaba seleccionada)
            if (grupoSeleccionado === areaId) {
                grupoSeleccionado = null;
                nombreSeleccionado = null;
            } else {
                grupoSeleccionado = areaId;
                nombreSeleccionado = areaNombre;
                this.classList.add('selected'); // Añadir clase 'selected'
            }

            // Actualizar el valor del input oculto con el ID seleccionado
            if (inputAreasSeleccionadas) {
                inputAreasSeleccionadas.value = grupoSeleccionado ? grupoSeleccionado : '';
            }

            // Mostrar el área seleccionada o "Ninguna" si no hay selección
            if (displaySeleccionadas) {
                displaySeleccionadas.textContent = nombreSeleccionado ? nombreSeleccionado : 'Ninguna';
            }
        });
    });
});

// Función para cerrar el modal al guardar la selección (opcional)
const guardarSeleccionBtn = document.getElementById('guardarSeleccionBtn');
guardarSeleccionBtn.addEventListener('click', function(event) {
    const modal = document.getElementById('miModal');
    if (modal) {
        modal.style.display = 'none';
    }
});
