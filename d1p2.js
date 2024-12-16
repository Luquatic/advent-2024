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

  let score = 0;

  left.forEach((x) => {
    let amount = 0;

    right.forEach((y) => {
      if (x === y) amount += 1;
    });

    if (amount !== 0) score += x * amount;
  });

  console.log(score);
}

calculateTotalDistance(input);
