#!/usr/bin/node
function incr(number) {
  return number + 1; // Increment the number
}

function incrementAndCall(number, theFunction) {
  const incrementedValue = incr(number); // Use the incr function to increment
  theFunction(incrementedValue); // Call the provided function with the incremented value
}

// Example usage:
function displayValue(value) {
  console.log("The incremented value is:", value);
}

// Call incrementAndCall with 5 and displayValue function
incrementAndCall(5, displayValue);
