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
  def procurar(self, chave, no = None):
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

  def inserir(self, chave):
    raiz = self.raiz
    if len(raiz.chaves) == (2*self.ordem) - 1:                      # chaves cheias, dividir os filhos
      no = No()
      self.raiz = no
      no.filhos.inserir(0, raiz)
      self.dividirFilhos(no, 0)            
      self.inserirNaoCheio(raiz, chave)
    else:
      self.inserirNaoCheio(raiz, chave)

  def dividirFilhos(self, no: No, index):
    ordem = self.ordem
    filho = no.filhos[index]
    novoFilho = No(eFolha=filho.eFolha)

    # Move todos os filhos do nó envado por parâmetro para a direita a insere o nó na posição index+1.
    no.filhos.inserir(index + 1, novoFilho)
    no.chaves.inserir(index, filho.chaves[ordem - 1])

    # chaves do novo filho são da ordem até (2 * ordem) - 1
    # filho é de 0 até ordem - 2
    novoFilho.chaves = filho.chaves[ordem : (2 * ordem - 1)]
    filho.chaves = filho.chaves[ 0 : (ordem - 1)]

    # Filhos de z são da ordem até 2 * ordem de filho.filhos
    if not filho.chaves:
      novoFilho.filhos = filho.filhos[ordem : ( 2 * ordem)]
      filho.filhos = filho.filhos[0 : (ordem - 1)]

  def inserirNaoCheio(self, no: No, chave):
    indexChavesNo = len(no.chaves) - 1

    if no.eFolha:
      #inserir a chave
      no.chaves.append(0)

      while indexChavesNo >= 0 and chave < no.chaves[indexChavesNo]:
        no.chaves[indexChavesNo + 1] = no.chaves[indexChavesNo]
        indexChavesNo -= 1

      no.chaves[indexChavesNo + 1] = chave
    else:
      # inserir filha
      while indexChavesNo >= 0 and chave < no.chaves[indexChavesNo]:
        indexChavesNo -= 1
      
      indexChavesNo += 1

      if len(no.filhos[indexChavesNo].chaves) == ( 2 * self.ordem) - 1:
        self.dividirFilhos(no, indexChavesNo)

        if chave > no.chaves[indexChavesNo]:
          i += 1

      self.inserirNaoCheio(no.filhos[indexChavesNo], chave)
