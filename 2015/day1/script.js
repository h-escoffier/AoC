
// read input
async function loadInput() {
  const response = await fetch("../data/input_day1.txt");
  const input = await response.text();
  return input;
}

// part1
async function part1() {
    let floor = 0
    const input = await loadInput();
    for (let i = 0; i < input.length; i++) {
        if (input[i] === "(") {
            floor++;
        }
        else {
            floor--;
        }
    }
    console.log(floor); 
}

part1();

// part2
async function part2() {
    let floor = 0
    const input = await loadInput();
    for (let i = 0; i < input.length; i++) {
        if (input[i] === "(") {
            floor++;
        }
        else {
            floor--;
        }
        // Part 2
        if (floor === -1) {
            console.log(floor);
            console.log(i + 1);
            break
        }
    }
}

part2();

// graphical representation (in progress)
async function tower() {
    let floor = 0; 
    const input = await loadInput();
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");


    let x = 0;
    let y = 200;

    ctx.beginPath();
    ctx.moveTo(x,y);

    for (let i = 0; i < input.length; i++) {
        if (input[i] === "(") {
            floor++;
        }
        else {
            floor--;
        }

        ctx.lineTo(i, y - floor);
    }

    ctx.strokeStyle = "red";
    ctx.lineWidth = 2;

    ctx.stroke();
}

tower()