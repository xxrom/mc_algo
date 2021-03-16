'''
access - None (you can't access 'i' item, 
          because there are no order in hash tables, 
          it's messy to understand why it is not defined ...)
search - O(1) (worse - O(N))
insert - O(1) (worser - O(N), 
          because it could check for the same key, 
          or it could try to find an empty spot 
          in table to place new data in)
delete - O(1) (worse - O(N))
'''


class HashTable:

  def __init__(self, size):
    self.data = [[]] * size

  def _hash(self, key):
    hash = 0

    for index, charItem in enumerate(key):
      # print(charItem, ord(charItem), len(self.data))
      hash = (hash + ord(charItem) * index) % len(self.data)

    return hash

  def set(self, key, value):
    dataIndex = self._hash(str(key))

    print(dataIndex)

    self.data[dataIndex].append({'key': key, 'value': value})

  def get(self, key):
    dataIndex = self._hash(str(key))

    ans = None

    currentBucket = self.data[dataIndex]

    for item in currentBucket:
      if item['key'] == key:
        ans = item['value']

    return ans


myHashTable = HashTable(50)

# print(myHashTable._hash('aljfdkl'))

myHashTable.set('banana', 10000332)
myHashTable.set('banana2', 10999)

print(myHashTable.get('banana'))
print(myHashTable.get('banana2'))
print(myHashTable.get('ba2'))
