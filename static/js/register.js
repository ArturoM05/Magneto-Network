console.log("dbisdvad")
// Obtener elementos
var modal = document.getElementById("miModal");
var btnAbrir = document.getElementById("abrirModal");
var spanCerrar = document.getElementsByClassName("cerrar")[0];
const guardarSeleccionBtn = document.querySelector('input[type="button"]');

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
    const areasSeleccionadas = [];  
    const nombresSeleccionados = [];  
    const inputAreasSeleccionadas = document.getElementById('areasSeleccionadas'); 
    const displaySeleccionadas = document.getElementById('areasSeleccionadasDisplay'); 

    fetch('/area_interes/show/')
        .then(response => response.json())
        .then(data => {
            const areasInteresList = document.getElementById('areasInteresList');
            data.areas_interes.forEach(area => {
                const li = document.createElement('li');
                li.textContent = area.nombre;
                li.setAttribute('data-id', area.id); 
                li.setAttribute('data-nombre', area.nombre); 
                li.addEventListener('click', function() {
                    const areaId = this.getAttribute('data-id');
                    const areaNombre = this.getAttribute('data-nombre');
                    
                    if (areasSeleccionadas.includes(areaId)) {
                        areasSeleccionadas.splice(areasSeleccionadas.indexOf(areaId), 1);
                        nombresSeleccionados.splice(nombresSeleccionados.indexOf(areaNombre), 1);
                        this.classList.remove('selected'); 
                    } else {
                        // Si no está, lo añadimos
                        areasSeleccionadas.push(areaId);
                        nombresSeleccionados.push(areaNombre);
                        this.classList.add('selected'); 
                    }

                    inputAreasSeleccionadas.value = areasSeleccionadas.join(',');

                    if (nombresSeleccionados.length > 0) {
                        displaySeleccionadas.textContent = nombresSeleccionados.join(', ');
                    } else {
                        displaySeleccionadas.textContent = 'Ninguna';
                    }
                });
                areasInteresList.appendChild(li);
            });
        })
        .catch(error => console.error('Error al cargar áreas de interés:', error));
});

document.getElementById('miModal').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombreArea = document.getElementById('areaInteresInput').value;

    fetch('/area_interes/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-CSRFToken': getCookie('csrftoken') 
        },
        body: `nombre_area=${nombreArea}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Área de interés guardada correctamente');
            // Opcionalmente, actualizar el DOM o cerrar el modal
            document.getElementById('miModal').style.display = 'none';
        }
    })
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

guardarSeleccionBtn.addEventListener('click', function(event) {
    modal.style.display = 'none';
});