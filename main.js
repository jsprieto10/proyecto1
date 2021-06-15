//alert('Hola Sebas, Sara y Yirlenys!!!');
var nombre = "Anyi Reyes";
var años   = 22;

/*
var concatenacion = nombre + " " + años;

var datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Tengo: ${años} años</h3>
`;

if(años >= 22){
    datos.innerHTML += '<h1>Eres joven aun</h1>';
}else{
    datos.innerHTML += '<h1>Ya estas muy joven</h1>';
}

for (var i = 2000; i<=2021; i++){
    //bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año: " + i;
}
*/
/*
function MuestraMiNombre(nombre, años){
    var datos = document.getElementById("datos");
    datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Tengo: ${años} años</h3>
    `;
}

MuestraMiNombre("Anyi Reyes WEB", 22);
*/

function MuestraMiNombre(nombre, años){
    var misDatos = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Tengo: ${años} años</h3>
    `;

    return misDatos;
}

function imprimir (){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Anyi Reyes", 22);
}

imprimir();

var nombres = ['Alejandra', 'Angélica', 'Zoe'];
//alert(nombres[1]);

document.write('<h1>Listado de nombres</h1>');
/*
for(i = 0; i < nombres.length; i++){
    document.write(nombres[i] + '</br/>');
}
*/
nombres.forEach((nombre) => {
    document.write(nombre + '<br/>');
});
//var datos = document.getElementById("datos");
//datos.innerHTML = concatenacion;

//document.write(concatenacion);

//document.write(nombre);
//document.write(años);






