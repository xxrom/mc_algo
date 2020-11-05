/*
 * Space complexity = O(1)
 * We care only additional space (without input values)
 */
const boooo = (n) => {
  // Added only 1 value (i)
  for (i = 0; i < n.length; i++) {
    console.log("boooo !!!");
  }
};

boooo([1, 2, 3, 4, 5]);

// ----------------------------------------------------------------

// SpaceComplexity = O(N)
const arrayOfHiNTimes = (n) => {
  let hiArray = [];
  for (i = 0; i < n; i++) {
    // +1 space complexity on each for step
    hiArray.push("hi");
  }

  return hiArray;
};

console.log(arrayOfHiNTimes(6));
