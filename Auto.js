class Auto{
    constructor (color, marca, modelo){
        this.estado = "Apagado";
        this.color = color;
        this.marca = marca;
        this.modelo = modelo;
        this.kilometraje = 0;
    }

    mostrarEstado() {
        console.log(`El auto ${this.marca} ${this.color} del año ${this.modelo} tiene un kilometraje de ${this.kilometraje}kms y está ${this.estado}` );
    }
}