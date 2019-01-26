/**
 * Given a date string, dateString, in the format MM/DD/YYYY,
 * find and return the day name for that date.
 * Each day name must be one of the following strings:
 * Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.
 * For example, the day name for the date 12/07/2016 is Wednesday.
 */

function getDayName(dateString) {
  let dayName;
  // Write your code here
  const daysOfTheWeak = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
  ];
  dayName = daysOfTheWeak[new Date(dateString).getDay()];
  console.log(dayName);
}

// Output
getDayName('10/11/2009'); // Sunday
getDayName('11/10/2010'); // Wednesday
