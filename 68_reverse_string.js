function reverse(str) {
  if (!str || str.length < 2 || typeof str !== 'string') {
    return str;
  }

  const totalItems = str.length - 1;
  const reversed = [];

  for (let i = totalItems; i > 0 ; i--) {
    reversed.push(str[i])
  }

  return reversed.join('');
}

console.log(reverse('reverse my name is Nikita!'))
