$(document).ready(function(){
      
function guardar(){
 
        
var cod,
elementCod = document.getElementById('codigo');
if (elementCod != null) {
    cod = elementCod.value;
}
else {
    cod = null;
}
var img,
elementImg = document.getElementById('imagen');
if (elementImg != null) {
    img = elementImg.value;
}
else {
    img = null;
}
var  nom
elementNom = document.getElementById('nombre');
if (elementNom != null) {
    nom = elementNom.value;
}
else {
    nom = null;
}
var  edad,
elementEdad = document.getElementById('edad');
if (elementEdad != null) {
    edad = elementEdad.value;
}
else {
    edad = null;
}
var  menu,
elementMenu = document.getElementById('menuDesplegable');
if (elementMenu != null) {
    menu = elementMenu.value;
}
else {
    menu = null;
}
var des,
elementDes = document.getElementById('descripcion');
if (elementDes != null) {
    des = elementDes.value;
}
else {
    des = null;
}






var fila="<tr><td>"+cod+"</td><td>"+img+"</td><td>"+nom+"</td><td>"+edad+"</td></tr>"+menu+"</td></tr>"+des+"</td></tr>";

    document.getElementById("tablita").innerHTML = fila;

}

function postTo(url, query) {
        var request = (XMLHttpRequest?new XMLHttpRequest():new ActiveXObject());
        request.open('POST', url, true);
        request.send(query);
}
guardar();
});