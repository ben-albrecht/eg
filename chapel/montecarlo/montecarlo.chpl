// Calcuate pi using a monte carlo simulation

use Random, Time;

config const n = 10000;
config const verbose: bool = false;

var count:int;
var pi, startTime, totalTime: real;
var rs = new RandomStream();

startTime = getCurrentTime(TimeUnits.microseconds);

// Find random points on the complex plane in (0..1+i)
// and count how many are outside the unit circle.
count = + reduce for 1..n do abs(rs.getNext()**2 + rs.getNext()**2):int;

// The probability a point is inside the unit circle is pi / 4.
pi = 4 * (n-count):real(64) / n;

// Write out the results
writeln(pi);
totalTime = (getCurrentTime(TimeUnits.microseconds) - startTime) / 1000000;
if (verbose) then
  writeln("Calculation took: ", totalTime, " seconds");

delete rs;

/*
// Monte Carlo simulation of Pi


// Generate random x and y values between 0 and 1

// Ratio of values inside circle (x^2 + y^2 <= 1) to outside circle (x^2 + y^2 > 1) is 1/pi
// therefore #(x^2 + y^2 > 1) / #(x^2 + y^2 >= 1) ~= pi

use Random, Time;

var pi, startTime, totalTime: real;

config const numTasks = here.numCores;

config const N = 1000000, seed = 314159;

var count:int;
var pi;
var rs = new RandomStream(seed);

startTime = getCurrentTime(TimeUnits.microseconds);

count = + reduce for 1..N do abs(rs.getNext()**2 + rs.getNext()**2):int;

pi = 4 * (n-count):real(64) / n;

writeln(pi);
totalTime = (getCurrentTime(TimeUnits.microseconds) - startTime) / 1000000;
if (verbose) then
  writeln("Calculation took: ", totalTime, " seconds");

delete rs;
*/
