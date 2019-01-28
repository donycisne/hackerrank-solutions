/**
 * Complete the function by returning a RegExp object, er,
 * that matches every integer in some string s.
 */

function regexVar(...s) {
  const re = /(\d)+/g;
  console.log(`➡ Integer Match : [${s}]`)
  s.forEach(e => {
    let numStart = e
    console.log(Math.floor(numStart));
    if (e % 1 !== 0) {
      let numEnd = parseInt((numStart + '').replace(/[1-9]./, ''));
      console.log(numEnd)
    }
  });
}

// Output
// regexVar(1, 2, 3);
regexVar(102, 1948948, 1.3, 4.5);
