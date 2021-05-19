

var btnCrear = document.getElementById("btn-create")

btnCrear.onclick = function(e){
    e.preventDefault();

    var inputNombre = document.getElementById("nom")
    var inputCali = document.getElementById("cali")
    var inputDuracion = document.getElementById("duracion")
    var inputAnio = document.getElementById("anio")




    var raw = JSON.stringify({"nombre":inputNombre.value,"duracion":inputDuracion.value,"calificacion":inputCali.value,"año":inputAnio.value});

    console.log(raw)
    var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
      },
    body: raw,
    mode: 'cors'
    };

    fetch("http://127.0.0.1:5000/pelicula", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));


    }