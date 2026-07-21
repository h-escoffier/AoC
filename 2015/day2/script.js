// read input
async function loadInput() {
  const response = await fetch("../data/input_day2.txt");
  const input = await response.text();
  return input;
}

// part1
async function part1() {
    let sumArea = 0;
    const input = await loadInput();
    const lines = input.split("\n");
    for (const line of lines) {
        const [l, w, h] = line.split("x");
        const area = 2*l*w + 2*w*h + 2*h*l;
        sumArea += area + smallestSize(l, w, h);
    }
    console.log(sumArea);
}

part1();

function smallestSize(l, w, h) {
    const a = l*w; 
    const b = l*h; 
    const c = w*h; 
    return Math.min(a, b, c);
}

// part2
async function part2() {
    let sumRibbon = 0;
    const input = await loadInput();
    const lines = input.split("\n");
    for (const line of lines) {
        const [l, w, h] = line.split("x");
        const ribbon = l*w*h;
        sumRibbon += ribbon + smallestFace(l, w, h);
    }
    console.log(sumRibbon);
}

part2();

function smallestFace(l, w, h) {
    const arr = [l, w, h];
    arr.sort((a, b) => a - b);
    return face = arr[0]*2 + arr[1]*2;
}