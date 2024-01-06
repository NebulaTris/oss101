function printPattern(rows) {
  for (let i = 1; i <= rows; i++) {
    let pattern = "";

    // Add spaces
    for (let j = 1; j <= rows - i; j++) {
      pattern += " ";
    }

    // Add stars
    for (let k = 1; k <= i; k++) {
      pattern += "*";
    }

    console.log(pattern);
  }
}

// Change the value of 'rows' to adjust the size of the pattern
const rows = 5;
printPattern(rows);
