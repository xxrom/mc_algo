// time - O(N^2), space - O(N^2)
const boxes = ["a", "b", "c", "d", "e"];
const pairs = [];

const logAllPairsOfArray = (array) => {
  const ansPairs = [];

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      ansPairs.push([array[i], array[j]]);
    }
  }

  return ansPairs;
};

console.log(logAllPairsOfArray(boxes));
