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
  //imprimir un strig POST
  console.log(requestOptions.method)


  fetch("http://127.0.0.1:5000/pelicula", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}

function mostrar_peliculas(){
  console.log("entro");
  fetch("http://127.0.0.1:5000/peliculas")
  .then(function (response) {
      return response.json();
  }).then(function (response){
      var div = document.getElementById("peliculas");
      var ul = document.createElement("ul");
      div.append(ul);
      console.log(ul);
      for(var pelicula of response.resultado){
        var li = document.createElement("li");
        li.innerText = pelicula.nombre;
        ul.append(li);
      }
  })
}

mostrar_peliculas();


//opciones para hacer prueva 
// alert.
//log.
