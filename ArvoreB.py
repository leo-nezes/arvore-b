from math import ceil
from No import No

class ArvoreB:
  def __init__(self, ordem):
    self.raiz = No()
    self.ordem = ordem
    self.numMaxFilhos = ordem
    self.numMinFilhos = ceil(ordem / 2)
    self.numMaxElementos = self.numMaxFilhos - 1
    self.numMinElementos = self.numMinFilhos - 1

  # Procura da chave na Árvore B.
  # chave - valor a ser procurado
  # no - nó onde se incia a busca
  def procura(self, chave, no = None):
    index = 0

    if isinstance(no, No):
      while index < len(no.chaves) and chave > no.chave[index]:     # verifca se a chave está entre as chaves do nó
        index += 1

        if index < len(no.chaves) and chave == no.chave[index]:     # nó encontrado
          return (no, index)
        elif no.eFolha:                                             # chave não encontrada e chegou na folha da árvore. Chave não exste na árvore
          return None
        else:                                                       # Procura no flho
          return self.procura(chave, no.chaves[index])
    else:                                                           # Nenhum nó informado, começa a busca pela raiz
      return self.procura(chave, self.raiz)
