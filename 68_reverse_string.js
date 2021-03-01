function reverse(str) {
  const arr = str.split('');
  arr.reverse();
  return arr.join('');
}

console.log(reverse('reverse my name is Nikita!'))
