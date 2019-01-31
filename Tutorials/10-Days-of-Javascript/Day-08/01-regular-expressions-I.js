/**
 * Complete the function by returning a RegExp object, re,
 * that matches any string s that begins and ends with the same vowel.
 * Recall that the English vowels are a, e, i, o, and u.
 */

function regexVar(s) {
  const re = /^([aeiou]).+\1$/;;

  const reIsTrue = s.match(re);

  if (reIsTrue) {
    console.log(`➡ '${s}' starts and ends with the same vowel: ${reIsTrue[1]}`);
  } else {
    console.log(`➡ '${s}' doesn't start and end with the same vowel.`);
  }
}

// Output
regexVar('adc') // false
regexVar('eadcae') // true
