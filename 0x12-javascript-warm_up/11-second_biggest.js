#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert arguments to numbers

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueArgs = Array.from(new Set(args)); // Remove duplicates
  uniqueArgs.sort((a, b) => b - a); // Sort in descending order
  console.log(uniqueArgs[1]); // Print the second biggest integer
}
