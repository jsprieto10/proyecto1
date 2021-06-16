alert('Hola Sebastian, Sara, Anyi!!');
var nombre = "Yirleny Perea Trellez";
var altura   = 160;

/*

var concatenacion = nombre + " " + altura;

//document.write(concatenacion);

//var datos = document.getElementById("datos");
//datos.innerHTML = (concatenacion);

var datos = document.getElementById("datos");
datos.innerHTML = `
<h1>Soy la caja de datos</h1>
<h2>Mi nombre es: ${nombre}</h2>
<h3>altura: ${altura} cm</h3>
`;

if(altura >= 170){
    datos.innerHTML += '<h1>Eres una persona ALTA</h1>';
}else{
    datos.innerHTML += '<h1>Eres una persona BAJITA</h1>';
}
    
for (var i = 1993; i<=2021; i++){
    //bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año: " + i;
}

*/

/*
function MuestraMiNombre(nombre, altura) {
    var datos = document.getElementById("datos");
    datos.innerHTML = `
       <h1>Soy la caja de datos</h1>
       <h2>Mi nombre es: ${nombre}</h2>
       <h3>altura: ${altura} cm</h3>
    `;
}

MuestraMiNombre("Yirleny Perea Trellez WEB", 160);
*/

function MuestraMiNombre(nombre, altura){
    var misDatos = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>altura: ${altura} cm</h3>
    `;

    return misDatos;
}

function imprimir (){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Yirleny Perea Trellez WEB", 160);
}

imprimir();

var nombres = ['Zunilda', 'Marleiza', 'Esther', 'Sandra', 'Ever'];
//alert(nombres[0]);

document.write('<h1>Listado de nombres</h1>');
/*
for(i = 0; i < nombres.length; i++){
    document.write(nombres[i] + '</br/>');
}
*/

nombres.forEach((nombre) => {
    document.write(nombre + '<br/>');
});





