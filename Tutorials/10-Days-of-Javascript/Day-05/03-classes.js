/**
 * Create a Polygon class that has the following properties:
 * A constructor that takes an array of integer values describing the lengths of the polygon's sides.
 * A perimeter() method that returns the polygon's perimeter.
 */

class Polygon {
  constructor(sides) {
    this.sides = sides;
  }
  perimeter() {
    return this.sides.reduce((a, b) => a + b);
  }
}

// Output
const triangle = new Polygon([3, 4, 5]);

console.log(`Sides ➡ ${triangle.sides}`);
console.log(`Perimeter ➡ ${triangle.perimeter()}`);
