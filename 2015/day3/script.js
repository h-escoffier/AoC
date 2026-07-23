// read input
async function loadInput() {
  const response = await fetch("../data/input_day3.txt");
  const input = await response.text();
  return input;
}

// animate 
import { animate, createTimeline } from "https://esm.sh/animejs";

const canvas = document.getElementById("path");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener("resize", resizeCanvas);
function resizeCanvas(){
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

// part1
async function part1(canvas) {
    const input = await loadInput();
    const ctx = canvas.getContext("2d");

    let x = 0;
    let y = 0;

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    ctx.beginPath();
    ctx.moveTo(centerX, centerY);

    // console.log(input);
    for (const move of input) {
        if (move === '>') {
            x++
        }
        else if (move === '<') {
            x--
        }
        else if (move === 'v') {
            y++
        }
        else if (move === '^') {
            y--
        }

        const scale = 0.6;

        const newX = centerX + x * canvas.width*scale/100;
        const newY = centerY - y * canvas.height*scale/100;

        ctx.lineTo(newX, newY);
        ctx.lineWidth = 5;
        ctx.stroke();

        animate('.square', {
            x: `${x * scale}vh`,
            y: `${-y * scale}vw`,
            duration: 1
        });

        await new Promise(resolve => setTimeout(resolve, 1));

    }
}

part1(canvas);


// const tl = createTimeline({ defaults: { duration: 1000 } });

// tl.label('start')
//   .add('.square',   { x: '15rem' }, 500)