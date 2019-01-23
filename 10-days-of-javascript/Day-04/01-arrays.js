/**
 * Complete the getSecondLargest function.
 * It has one parameter: an array, nums, of n numbers.
 * The function must find and return the second largest number in nums.
 */

function getSecondLargest(nums) {
  // Complete the function
  console.log(`The second max value in [${nums}] is
    ${[...new Set(nums)].sort((a, b) => b - a)[1]}`);
}

// Output
getSecondLargest([2, 93, 16, 26, 68]);
