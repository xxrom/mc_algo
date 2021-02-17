class MyArray:

  def __init__(self):
    self.data = {}
    self.length = 0

  def get(self, index):
    if index in self.data:
      return self.data[index]

    return None

  def push(self, item):
    self.data[self.length] = item
    self.length += 1

  def delete(self, deleteIndex):
    for i in range(deleteIndex, self.length - 1):
      self.data[i] = self.data[i + 1]

    del self.data[self.length - 1]
    self.length -= 1

  def pop(self):
    del self.data[self.length - 1]
    self.length -= 1


arr = MyArray()

print(arr.get(0))

arr.push('TTT')

print(arr.get(0))

arr.push('ggg')

print(arr.get(1))

arr.pop()

print(arr.get(1))
print(arr.get(0))
arr.delete(0)
print(arr.get(0))
