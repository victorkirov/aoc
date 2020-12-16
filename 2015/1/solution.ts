const fs = require('fs')

const data = fs.readFileSync('input', 'utf8')

let floor = 0
for (let c in data) {
  if(data[c] == '(') floor++
  if(data[c] == ')') floor--
}

console.log(floor)

floor = 0
for (let c in data) {
  if(data[c] == '(') floor++
  if(data[c] == ')') floor--

  if (floor === -1) {
    console.log(parseInt(c) + 1)
    break
  }
}
