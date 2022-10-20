from xml.etree import ElementInclude


def findTheWinner(n, k):
  friends = []
  for i in range(0, n):
    friends += [i + 1]

  def eliminateFriends(list, index=0):
    if len(list) == 1:
      return print(list[0])
    
    index += k - 1
    if index >= len(list):
      index %= len(list)

    list.pop(index)
    return eliminateFriends(list, index)

  return eliminateFriends(friends)

findTheWinner(5, 2)
findTheWinner(6, 5)