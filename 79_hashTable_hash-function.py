class HashTable:

  def __init__(self, size):
    self.data = [[]] * size

  def _hash(self, key):
    hash = 0

    for charItem in key:
      # print(charItem, ord(charItem), len(self.data))
      hash = (hash + ord(charItem)) % len(self.data)

    return hash

  def set(self, key, value):
    dataIndex = self._hash(str(key))

    print(dataIndex)

    self.data[dataIndex].append({'key': key, 'value': value})

  def get(self, key):
    dataIndex = self._hash(str(key))

    ans = None

    for item in self.data[dataIndex]:
      if item['key'] == key:
        ans = item['value']

    return ans


myHashTable = HashTable(50)

# print(myHashTable._hash('aljfdkl'))

myHashTable.set('banana', 10000332)
myHashTable.set('banana2', 10999)

print(myHashTable.get('banana'))
print(myHashTable.get('banana2'))
