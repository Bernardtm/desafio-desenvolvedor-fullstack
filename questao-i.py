#! /usr/bin/python
#QUESTAO I

#Dado um array de numeros inteiros, retorne os indices dos
#dois numeros de forma que eles se somem a um alvo
#especifico.

#Voce pode assumir que cada entrada teria exatamente uma
#solucao, e voce nao pode usar o mesmo elemento duas
#vezes.

#EXEMPLO

#Dado nums = [2, 7, 11, 15], alvo = 9,
#Como nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def getIndexesThatTheSumIsEqualTheTarget(numbers, target):
  for index1 in range(0, len(numbers) - 1):
    for index2 in range (index1 + 1, len(numbers)):
      if target == (numbers[index1] + numbers[index2]):
        return [index1, index2]


nums = [2, 8, 11, 15, 3, 7]
target = 9

print(getIndexesThatTheSumIsEqualTheTarget(nums, target))