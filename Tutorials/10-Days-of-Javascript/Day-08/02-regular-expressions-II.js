/**
 * Complete the function by returning a RegExp object, re,
 * that matches any string s satisfying both of the following conditions:
 * - String s starts with the prefix Mr., Mrs., Ms., Dr., or Er.
 * - The remainder of string s (i.e., the rest of the string after the prefix)
 *   consists of one or more upper and/or lowercase English alphabetic letters (i.e., [a-z] and [A-Z]).
 */

function regexVar(s) {
  const re = /^(Mr?s|[MDE]r)\.[a-zA-Z]+$/;

  const reIsTrue = s.match(re);

  if (reIsTrue) {
    console.log(`- ${s} ➡ Match`)
  } else {
    console.log(`- ${s} ➡ Does not match`)
  }
}

// Output
regexVar('Mr.X'); // True
regexVar('Dr#X'); // False
