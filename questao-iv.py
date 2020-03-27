#! /usr/bin/python
#QUESTAO IV

#Dados n inteiros nao negativos representando um mapa de
#elevacao onde a largura de cada barra e 1, calcule quanta
#agua e capaz de reter apos a chuva.

#EXEMPLO

#Input: [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6

def getWaterQuantity(heights):
  leftIndex = 0
  rightIndex = len(heights) - 1
  waterQuantity = 0
  leftMaxHeight = 0
  rightMaxHeight = 0

  while (leftIndex < rightIndex):
    if (heights[leftIndex] < heights[rightIndex]):
      if (heights[leftIndex] >= leftMaxHeight):
        leftMaxHeight = heights[leftIndex]
      else:
        waterQuantity += (leftMaxHeight - heights[leftIndex])
      leftIndex += 1
    else:
      if (heights[rightIndex] >= rightMaxHeight):
        rightMaxHeight = heights[rightIndex]
      else:
        waterQuantity += (rightMaxHeight - heights[rightIndex])
      rightIndex -= 1
  return waterQuantity

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

print(getWaterQuantity(heights))