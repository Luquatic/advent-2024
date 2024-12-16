const fs = require('fs');

// Read the content of input.txt synchronously
const input = fs.readFileSync('./input.txt', 'utf-8');

function calculateTotalDistance(input) {
  const left = []
  const right = []

  const lines = input.trim().split('\n');

  lines.forEach(line => {
    const [a, b] = line.trim().split(/\s+/).map(Number);
    left.push(a);
    right.push(b);
  });

  left.sort((a, b) => a - b);
  right.sort((a, b) => a - b);

  let totalDistance = 0;

  for (let i = 0; i < left.length; i++) {
    totalDistance += Math.abs(left[i] - right[i]);
  }

  console.log(totalDistance);
}

calculateTotalDistance(input);
