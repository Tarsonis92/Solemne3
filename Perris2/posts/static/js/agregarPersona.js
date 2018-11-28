$(document).ready(function(){

function validar(){

 var nombre,apellido,rut,email,date,numTel,region,ciudad,vivienda,username,contra;

 var array = [nombre,apellido,rut,email,date,numTel,region,ciudad,vivienda,username,contra];

 nombre = document.getElementById("nombre").value;
 apellido = document.getElementById("apellido").value;
 rut = document.getElementById("rut").value;
 email = document.getElementById("email").value;
 date = document.getElementById("date").value;
 numTel = document.getElementById("numTel").value;
 username = document.getElementById("username").value;
 contra = document.getElementById("contra").value;

 if(nombre==="" || apellido==="" || rut==="" || email==="" || date==="dd/mm/yyyy" || numTel==="" || username==="" || contra===""){
       alert("Debe llenar todos los campos");
       return false;
 }
 
}

    });