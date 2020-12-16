const fs = require('fs')

const data = fs.readFileSync('input', 'utf8').trim()

function getNextPosition(instruction, x, y) {
  switch(instruction) {
    case '<':
      return [x - 1, y]
    case '>':
      return [x + 1, y]
    case '^':
      return [x, y + 1]
    case 'v':
      return [x, y - 1]
    default:
      throw new Error(`unknown instruction ${instruction}`)
  }
}

// == part 1 ==
{
  const visited = new Set()

  let x = 0
  let y = 0

  visited.add(`${x}_${y}`)

  for(let i = 0; i < data.length; i++) {
    const instruction = data[i]

    const [xn, yn] = getNextPosition(instruction, x, y)
    x = xn
    y = yn

    visited.add(`${x}_${y}`)
  }

  console.log(Array.from(visited).length)
}

// == part 2 ==
{
  const visited = new Set()

  let x = y = rx = ry = 0

  visited.add(`${x}_${y}`)

  for(let i = 0; i < data.length; i+=2) {
    const santaInstruction = data[i]
    const roboInstruction = data[i + 1]

    let [xn, yn] = getNextPosition(santaInstruction, x, y)
    x = xn
    y = yn

    visited.add(`${x}_${y}`)

    let [rxn, ryn] = getNextPosition(roboInstruction, rx, ry)
    rx = rxn
    ry = ryn

    visited.add(`${rx}_${ry}`)
  }

  console.log(Array.from(visited).length)
}
