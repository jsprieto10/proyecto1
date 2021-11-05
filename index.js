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
      var tabla = document.createElement("table");
      div.append(tabla);
      console.log(tabla);
      for(var pelicula of response.resultado){
        <table>
          <tr>
          <td>Nombre</td>
          <td>Calificación</td>
          <td>Duración</td>
          <td>Año</td>
        </tr>
        </table>
        var td = document.createElement("td");
        td.innerText = pelicula.nombre;

        tabla.append(tr);
      }
  })
}

mostrar_peliculas();


//opciones para hacer prueva 
// alert.
//log.

//<table>
//<tr>
//<th>Nombre</th>
//<th>Calificación</th>
//<th>Duración</th>
//<th>Año</th>
//</tr>
//<tr>
//<td>Up, una aventura del altura</td>
//<td>5</td>
//<td>136</td>
//<td>2009</td>
//</tr>
//</table>
