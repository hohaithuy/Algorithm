#Anh giao hang
possiblePath = []
sumPath = []

def findPath(array, path, soDinh, sum):
  if len(path) == soDinh and (path not in possiblePath):
    possiblePath.append(path.copy())
    for j in array:
      if j[1] == path[0] and j[0] == path[-1]:
        sumPath.append(sum + int(j[2]))
        break
    return

  pos = path[-1]
  for i in array:
    if pos == i[0] and (i[1] not in path):
      path.append(i[1])
      findPath(array, path, soDinh, sum + int(i[2]))
      path.pop()



n, start =map(str, input().split())
n = int(n)

array = []

for i in range(n):
  p = list(map(str, input().strip().split()))[:3]
  array.append(p)

allDinh = []
for i in array:
  if i[0] not in allDinh:
    allDinh.append(i[0])

soDinh = len(allDinh)
path = []
path.append(start)

findPath(array, path, soDinh, 0)

min = sumPath[0]
index = -1
for i in range(len(sumPath)):
  if sumPath[i] < min:
    min = sumPath[i]
    index = i

for i in range(soDinh):
  print(possiblePath[index][i], end = ' ')
print(possiblePath[index][0])