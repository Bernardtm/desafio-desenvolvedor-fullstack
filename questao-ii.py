#! /usr/bin/python
#QUESTAO II

#Um bracket e considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].

#Dois brackets sao considerados um par combinado se o bracket de abertura (isto
#e, (, [ou {) ocorre a esquerda de um bracket de fechamento (ou seja,),] ou} do
#mesmo tipo exato. Existem tres tipos de pares de brackets : [ ], { } e ( ).

#Um par de brackets correspondente nao e balanceado se o de abertura e o de
#fechamento nao corresponderem entre si. Por exemplo, { [ ( ] ) } nao e balanceado
#porque o conteudo entre {e} nao e balanceado. O primeiro bracket inclui o de
#abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].

#Dado sequencias de caracteres, determine se cada sequencia de brackets e
#balanceada. Se uma string estiver balanceada, retorne SIM. Caso contrario, retorne
#NAO.

#EXEMPLO

#{[()]} SIM
#{[(])} NAO
#{{[[(())]]}} SIM

def isBracketStringBalanced(brackets, bracketPairs):
  length = len(brackets)
  for index in range(0, (length / 2)):
    if bracketPairs[brackets[index]] != brackets[length - index - 1]:
      return "NAO"
  return "SIM"

bracketPairs = {
  "{": "}",
  "[": "]",
  "(": ")"
}

brackets = "{[()]}"

print(isBracketStringBalanced(brackets, bracketPairs))

brackets = "{[(])}"

print(isBracketStringBalanced(brackets, bracketPairs))

brackets = "{{[[(())]]}}"

print(isBracketStringBalanced(brackets, bracketPairs))

