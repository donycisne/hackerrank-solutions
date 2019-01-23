/**
 * Complete the vowelsAndConsonants function.
 * It has one parameter, a string, s, consisting of lowercase English alphabetic letters (i.e., a through z).
 * The function must do the following:
 * 1 - Print each vowel in s on a new line.
 *     The English vowels are a, e, i, o, and u,
 *     and each vowel must be printed in the same order as it appeared in s
 * 2 - Print each consonant (i.e., non-vowel)
 *     in s on a new line in the same order as it appeared in s.
 */

function vowelsAndConsonants(s) {
  // For Loop
  const vowels = 'aeiou';
  let consonants = '';

  for (let i = 0; i < s.length; i++) {
    vowels.includes(s[i]) ? console.log(s[i]) : (consonants += s[i] + '\n');
  }
  console.log(consonants.trim());

  // Map
  // const vowels = [];
  // const consonants = [];
  // console.time('map');
  // [...s].map(i => ('aeiou'.includes(i) ? vowels.push(i) : consonants.push(i)));

  // vowels.map(v => console.log(v));
  // consonants.map(c => console.log(c));
  // console.timeEnd('map');
}

// Output
vowelsAndConsonants('javascriptloops');
