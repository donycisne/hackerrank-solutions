/**
 * Implement a function named factorial that has one parameter: an integer, n.
 * It must return the value of n! (i.e.,n factorial).
 */

function factorial(n) {
  let f = 1;
  if (n < 0) {
    console.log(`Factorial of ${n} is -1`);
  } else {
    for (let i = 1; i <= n; i++) {
      f *= i;
    }
    console.log(`Factorial of ${n} is ${f}`);
  }
  // Optional
  // if (n < 0) return -1;
  // return n === 0 ? 1 : n * factorial(n - 1);
}

// Output
factorial(4);

//Optional
// console.log(factorial(4));
