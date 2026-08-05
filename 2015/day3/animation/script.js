// read input
async function loadInput() {
//   const response = await fetch("input_day3_test.txt");
  const response = await fetch("../../data/input_day3.txt");
  const input = await response.text();
  return input;
}

// animate 
import { animate, createTimeline } from "https://esm.sh/animejs";

const visitCounts = new Map();
const maxCount = 5

function calculateSize(input) {

    let x = 0;
    let y = 0;
    let xMin = 0;
    let xMax = 0;
    let yMin = 0;
    let yMax = 0;

    for (const move of input) {
        
        if (move === '>') {
            x++
            if (x >= xMax) {
                xMax = x
            }
        }
        else if (move === '<') {
            x--
            if (x <= xMin) {
                xMin = x
            }
        }
        else if (move === 'v') {
            y--
            if (y <= yMin) {
                yMin = y
            }
        }
        else if (move === '^') {
            y++
            if (y >= yMax) {
                yMax = y
            }
        }
    }
    return [xMin, xMax, yMin, yMax]
}

function countToColor(count, maxCount) {
  const ratio = Math.min(count / maxCount, 1);
//   const ratio = Math.min(count / 20, 1);
  const start = { r: 144, g: 238, b: 144 }; 
  const end   = { r: 220, g: 20,  b: 20  }; 

  const r = Math.round(start.r + (end.r - start.r) * ratio);
  const g = Math.round(start.g + (end.g - start.g) * ratio);
  const b = Math.round(start.b + (end.b - start.b) * ratio);

  return `rgb(${r}, ${g}, ${b})`;
}

// part1
async function part1() {
    const input = await loadInput();
    const [xMin, xMax, yMin, yMax] = calculateSize(input)

    let nbRows = xMax - xMin + 1 
    let nbCols = yMax - yMin + 1 
    
    rendergrid(nbCols, nbRows)

    let x = 0;
    let y = 0;

    for (const move of input) {
        if (move === '>') {
            x++
        }
        else if (move === '<') {
            x--
        }
        else if (move === 'v') {
            y--
        }
        else if (move === '^') {
            y++
        }

        let col = y - yMin + 1;
        let row = x - xMin + 1;

        const cell = document.getElementById(`cell-${row}-${col}`);
        const count = (visitCounts.get(`cell-${row}-${col}`) ?? 0) + 1;
        visitCounts.set(`cell-${row}-${col}`, count);

        // cell.style.transform = `translateZ(${count * 1}px)`;
        cell.style.backgroundColor = countToColor(count, maxCount);
        cell.style.filter = `brightness(${Math.min(1 + count * 0.15, 3)})`;
        // cell.animate(
        //     [
        //     { transform: 'translateZ(0px)' },
        //     { transform: 'translateZ(60px)'},
        //     { transform: 'translateZ(0px)' },
        //     ],
        //     {
        //     duration: 1200,
        //     easing: 'ease-in-out',
        //     iterations: 1
        //     }
        // );
        
        const totalDuration = 1000; 
        const delay = Math.max(1, totalDuration / input.length);
        await new Promise(resolve => setTimeout(resolve, 0.1));

    }
}

part1();

const container = document.querySelector(".m-grid");
const pixelSize = 50;

function rendergrid(nbCols, nbRows) {
    const width = window.innerWidth;
    const height = window.innerHeight;

    console.log(width, height)

    let cellHeight =  (height / 1.5) / nbRows
    let cellWidth  =  (width / 1.5) / nbCols

    if (cellWidth > cellHeight) {
        cellWidth = cellHeight
    } else if (cellHeight > cellWidth) {
        cellHeight = cellWidth
    }

    console.log(cellHeight, cellHeight)

    container.style.gridTemplateColumns = `repeat(${nbCols}, ${cellWidth}px)`;
    container.style.gridAutoRows = `${cellHeight}px`;
    container.style.gap = "1px";
    container.style.display = "grid";

    for (let row = 1; row <= nbRows; row++) {
        for (let col = 1; col <= nbCols; col++) {
            const cell = document.createElement("i");
            cell.classList.add("cell");
            cell.style.borderRadius = `${cellWidth * 0.1}px`;
            cell.id = `cell-${row}-${col}`;
            cell.style.width = `${cellWidth}px`;
            cell.style.height = `${cellHeight}px`;
            // cell.textContent = cell.id;
            container.appendChild(cell);
        }
    }

    console.log(nbRows, nbCols);
    console.log(container.children.length);
}

// rendergrid()