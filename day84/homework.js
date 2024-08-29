function Car(make, model, year, color) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.color = color;

    this.displayInfo = function() {
        console.log(`Car: ${this.make} ${this.model}, Year: ${this.year}, Color: ${this.color}`);
    };
}
let myCar = new Car('Toyota', 'Corolla', 2020, 'Red');
myCar.displayInfo();


let car1 = new Car('Honda', 'Civic', 2018, 'Blue');
let car2 = new Car('Ford', 'Mustang', 2021, 'Black');
car1.displayInfo();
car2.displayInfo();
