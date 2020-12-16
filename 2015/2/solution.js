const fs = require('fs')

const data = fs.readFileSync('input', 'utf8').trim().split('\n')

// == part 1 ==

const totalArea = data.reduce((result, line) => {
    const dimensions = line.split('x')

    let smallest = Infinity
    let area = 0

    for(let i = 0; i < dimensions.length - 1; i++) {
      const a = parseInt(dimensions[i])

      for(let j = i + 1; j < dimensions.length; j++) {
        const b = parseInt(dimensions[j])
        const sideArea = a * b

        if(smallest > sideArea) smallest = sideArea
        area += sideArea * 2
      }
    }

    return result + area + smallest
  }, 0)

console.log(totalArea)

// == part 2 ==
const totalRibbon = data.reduce((result, line) => {
    const dimensions = line.split('x')

    let smallest = Infinity

    for(let i = 0; i < dimensions.length - 1; i++) {
      const a = parseInt(dimensions[i])

      for(let j = i + 1; j < dimensions.length; j++) {
        const b = parseInt(dimensions[j])
        const sideLength = a + b

        if(smallest > sideLength) smallest = sideLength
      }
    }

    let volume = 1
    for(let i = 0; i < dimensions.length; i++) {
      volume *= parseInt(dimensions[i])
    }

    const perimeter = smallest * 2

    return result + perimeter + volume
  }, 0)

  console.log(totalRibbon)
