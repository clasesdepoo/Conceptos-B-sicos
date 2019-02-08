import Auto from "./Auto.js";

let auto1 = new Auto("Ford", 2001, "Rojo", 100);
let auto2 = new Auto("Nissan", 2020, "Transparente");
let auto3 = new Auto("Atom", 1384);

console.log(`Color ${auto1.color}`);//Lectura
console.log(`Color ${auto2.color}`);//Lectura
auto1.color = "Amarillo";//Escritura
auto2.color = "Azul";//Escritura

auto2.encender();
auto3.encender();
auto1.encender();
auto1.avanzar(50,2);
auto1.apagar();
auto1.avanzar(20, 1);