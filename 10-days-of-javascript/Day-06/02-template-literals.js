/**
 * The code has a tagged template literal that passes the area and perimeter
 * of a rectangle to a tag function named sides.
 * Recall that the first argument of a tag function is an array of string literals
 * from the template, and the subsequent values are the template's respective expression values.
 *
 * Complete the function in the editor so that it does the following:
 * 1 - Finds the initial values of S1 and S2 by plugging the area and perimeter values into the formula:
 *
 * S = (P ± -/(P² - 16 * A)) / 4
 *
 * where A is the rectangle's area and P is its perimeter.
 * 2 - Creates an array consisting of S1 and S2 and sorts it in ascending order.
 * 3 - Returns the sorted array.
 */

function sides(literals, ...expressions) {
  // Solution for HackerRank
  // const [A, P] = expressions;
  // const root = Math.sqrt(P ** 2 - 16 * A);
  // const s1 = (P + root) / 4;
  // const s2 = (P - root) / 4;

  // return [s1, s2].sort();

  // My Solution ✨
  const [[A, P]] = expressions;

  const root = Math.sqrt(P ** 2 - 16 * A);

  const s1 = (P + root) / 4;
  const s2 = (P - root) / 4;

  console.log(`${literals[0]}${A} ${literals[1]}${P}`);
  console.log(`\nFormula:\n S1 ➡ ${s1}\n S2 ➡ ${s2}`);
}

// Output
sides(['The area is: ', '.\nThe perimeter is: ', '.'], [10, 14]);
