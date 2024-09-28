#!/usr/bin/node
function incrementAndCall(number, theFunction) {
  const incrementedValue = number + 1; // Increment the number
  theFunction(incrementedValue); // Call the provided function with the incremented value
}

// Example usage:
function displayValue(value) {
  console.log("The incremented value is:", value);
}

// Call incrementAndCall with 5 and displayValue function
incrementAndCall(5, displayValue);
