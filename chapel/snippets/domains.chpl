// Messing with domains

// Create domain of indices 0-10
var D: domain(1) = {0..10 by 2};

// Create array using domain and with values 1-10
var array: [D] int = {0..20 by 4};
// Interestingly, {1..2} and {1..11} result in same histogram...

writeln(array);
