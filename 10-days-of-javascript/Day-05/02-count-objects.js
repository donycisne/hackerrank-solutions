/**
 * Complete the function getCount.
 * It has one parameter: an array, a, of objects.
 * Each object in the array has two integer properties denoted by x and y.
 * The function must return a count of all such objects o in array a that satisfy o.x == o.y.
 */

function getCount(objects) {
  let count = 0;
  for (let i = 0; i < objects.length; i++) {
    if (objects[i].x === objects[i].y) {
      count++;
    }
  }
  console.log(
    `The count of the total number of objects 'o' satisfying ➡ o.x === o.y is: ${count}`
  );

  // Optional
  // console.log(objects.filter(o => o.x === o.y).length);
}

// Output
getCount([{ x: 1, y: 1 }, { x: 2, y: 3 }, { x: 3, y: 3 }, { x: 3, y: 4 }]);
