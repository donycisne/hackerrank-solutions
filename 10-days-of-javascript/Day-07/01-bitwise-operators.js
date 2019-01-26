/**
 * We define S to be a sequence of distinct sequential integers
 * from 1 to n; in other words, S = {1,2,3,...,n}.
 * We want to know the maximum bitwise AND value of any two integers,
 * a and b (where a < b), in sequence S that is also less than a given integer, k.
 */

function getMaxLessThanK(n, k) {
  console.log(n < (k | (k - 1)) ? k - 2 : k - 1);
}

// Output
getMaxLessThanK(5, 2); // 1
getMaxLessThanK(8, 5); // 4
getMaxLessThanK(2, 2); // 0
