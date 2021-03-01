def mergeSortedArrays(arr0=[], arr1=[]):
  if type(arr0) is not list or type(arr1) is not list:
    return []

  if len(arr0) > 0 and len(arr1) == 0:
    return arr0
  if len(arr0) == 0 and len(arr1) > 0:
    return arr1

  sorted = []

  i0 = 0
  i1 = 0

  while i0 < len(arr0) and i1 < len(arr1):
    if arr0[i0] < arr1[i1] and i0 < len(arr0):
      sorted.append(arr0[i0])
      i0 += 1
    elif i1 < len(arr1):
      sorted.append(arr1[i1])
      i1 += 1

  return sorted


print(mergeSortedArrays([0, 3, 4, 31], 'asdf'))
print(mergeSortedArrays(324, 'asdf'))
print(mergeSortedArrays(324))
print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))
print(mergeSortedArrays([0, 3, 4, 31], []))
print(mergeSortedArrays([], [123, 1234, 12333]))
