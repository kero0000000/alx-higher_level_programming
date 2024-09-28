#!/usr/bin/node
function executeXTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Example usage:
function sayHello() {
  console.log("Hello!");
}

// Execute sayHello 3 times
executeXTimes(3, sayHello);
