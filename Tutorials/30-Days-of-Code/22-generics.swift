/*
Task:
  Write a single generic function named printArray;
    this function must take an array of generic elements as a parameter
    (the exception to this is C++, which takes a vector).
    The locked Solution class in your editor tests your function.
Note:
  You must use generics to solve this challenge.
  Do not write overloaded functions.
*/

import Foundation

struct Printer<T> {
	/**
	*  Name: printArray
	*  Print each element of the generic array on a new line.
  *  Do not return anything.
	*  @param A generic array
	**/

	// Write your code here

  // Solution
  func printArray(array: Array<T>) {
    for item in array {
      print(item);
    }
  }

}

// var n = Int(readLine()!)!
// var intArray = Array(repeating: 0, count: n);
// for i in 0...n - 1 {
// 	intArray[i] = Int(readLine()!)!;
// }

// n = Int(readLine()!)!
// var stringArray = Array(repeating: "", count: n);
// for i in 0...n - 1 {
// 	stringArray[i] = readLine()!;
// }

// Printer<Int>().printArray(array: intArray)
// Printer<String>().printArray(array: stringArray)
