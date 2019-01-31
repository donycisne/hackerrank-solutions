/**
 * Complete the following functions:
 * 1 - getArea(length, width):
 *     Calculate and return the area of a rectangle having sides length and width.
 * 2 - getPerimeter(length, width):
 *     Calculate and return the perimeter of a rectangle having sides length and width.
 */

function getArea(length, width) {
  let area;
  // Write your code here
  area = length * width;
  return area;
}

function getPerimeter(length, width) {
  let perimeter;
  // Write your code here
  perimeter = (length + width) * 2;
  return perimeter;
}

// Output
console.log('Area ➡', getArea(2, 3));
console.log('Perimeter ➡', getPerimeter(2, 3));
