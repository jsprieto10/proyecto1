// asigarnle una funcion al boton crear pelicula
// 1. ubijcarme en el boton
var btnCreate = document.getElementById("btn-create");
// escribir la función
btnCreate.onclick = function(e){
e.preventDefault();
// obtener los valores de los campos
var nombre = document.getElementById("nom").value;
var calificacion = document.getElementById("cali").value;
var duracion = document.getElementById("duracion").value;
var anio = document.getElementById("anio").value;

// hacer petición
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"nombre":nombre,"duracion":duracion,"calificacion":calificacion,"anio":anio});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/pelicula", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
}

//opciones para hacer purva 
// alert.
//log.
