#! /usr/bin/python
#QUESTAO III

#Digamos que voce tenha um array para o qual o elemento i
#e o preco de uma determinada acao no dia i.

#Se voce tivesse permissao para concluir no maximo uma
#transacao (ou seja, comprar uma e vender uma acao), crie
#um algoritmo para encontrar o lucro maximo.

#Note que voce nao pode vender uma acao antes de
#comprar.

#EXEMPLO

#Input: [7,1,5,3,6,4]
#Output: 5 (Comprou no dia 2 (preco
#igual a 1 ) e vendeu no dia 5 (preco
#igual a 6 ), lucro foi de 6 menos 1 = 5

#Input: [7,6,4,3,1]
#Output: 0 (Nesse caso nenhuma
#transacao deve ser feita, lucro maximo
#igual a 0)

def getMaximumDifferenceInOrder(numbers):
  highestDifference = 0
  for index1 in range(0, len(numbers)):
    for index2 in range(index1, len(numbers)):
      difference = numbers[index2] - numbers[index1]
      if highestDifference < difference:
        highestDifference = difference
  return highestDifference

    

stockValues = [7,1,5,3,6,4]

print(getMaximumDifferenceInOrder(stockValues))

stockValues = [7,6,4,3,1]

print(getMaximumDifferenceInOrder(stockValues))