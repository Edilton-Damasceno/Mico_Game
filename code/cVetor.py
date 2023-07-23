# # Lab 02 - Criando um TAD Vetor

import random
import array


# *******************************************************
# ***                                                 ***
# *******************************************************
class cVetor:

    # *******************************************************
    def __init__(self, n):
        self.vet = [0] * n
        self.count = 0
        self.quant = n

    def __str__(self):
        '''Formata a saida do vetor. Ex: <0, 0, 0, 0, 0>.'''
        return '<' + str(self.vet)[1:-1] + '>'

    def __getitem__(self, j):
        '''Retorna o número que está no indice passado.'''
        return self.vet[j]

    def __setitem__(self, j, k):
        '''Coloca um número no indice passado.'''

        self.vet[j] = k
        self.count += 1

    def tamanho(self):
        '''Retorna a quantidade de números colocados no vetor.'''
        return self.count

    def minimo(self):
        '''Retorna o menor número do vetor.'''

        for c in range(self.quant):
            if c == 0:
                min = self.vet[0]
            for v in range(self.quant):
                if self.vet[v] < self.vet[c] and self.vet[v] < min:
                    min = self.vet[v]
        return min

    def maximo(self):
        '''Retorna o maior número do vetor.'''
        for c in range(self.quant):
            if c == 0:
                max = self.vet[0]
            for v in range(self.quant):
                if self.vet[v] > self.vet[c] and self.vet[v] > max:
                    max = self.vet[v]
        return max

    def inserir(self, n):

        '''incrementa mais um número no vetor, aumentando o espaço na memoria Ex: <0,0> --> <0,0,0>.'''
        u = cVetor(1)
        u[-1] = n
        self.vet += u
        self.quant += 1
        print('\nA operação de inserção foi realizada com sucesso.\n')

    def invert(self):
        '''Inverte o vetor.'''
        l = self.vet[:]
        cc = 0
        for f in range(self.quant - 1, -1, -1):
            l[f] = self.vet[cc]
            cc += 1
        z = cVetor(self.quant)
        for r in range(self.quant):
            z[r] = l[r]
        return z

    def busca(self, chave_de_busca):
        '''Busca a primeira ocorrencia do número passado no vetor.'''
        funcionou = False
        for c in range(self.quant):
            if self.vet[c] == chave_de_busca:                
                indice = c
                funcionou = True
                break
        if funcionou:
            print('\nA operação de busca foi realizada com sucesso.\n')
        else:
            print('\nA operação de busca não foi realizada.\n')
        return indice
    
    def ocorrencias(self, chave):
        '''Retorna quantas vezes o número passado se repete'''
        ocorrencia = 0
        for c in range(self.quant):
                    if self.vet[c] == chave:                
                        ocorrencia += 1
        return ocorrencia

    def remove(self, chave):
        '''Remove o primeiro número passado do vetor.'''
        funcionou = False
        for c in range(self.quant):
            if self.vet[c] == chave:                
                self.vet[c] = 0
                funcionou = True
                break
        if funcionou:
            print('\nA operação de remção foi realizada com sucesso.\n')
        else:
            print('\nA operação de remção não foi realizada.\n')

    def gerarEstatisticas(self):
        '''Média.'''
        soma = 0
        for n, m in enumerate(self.vet):
            soma += m
        media = soma / self.quant

        '''Desvio Padrão.'''
        numerador = 0
        for j, k in enumerate(self.vet):
            numerador += (k - media)**2
        variancia = numerador / self.quant
        desvPad = variancia**0.5

        return media, desvPad

    def eIdentico(self, other):
        correspondente = True
        count = 0
        while correspondente and count < self.quant:
            if self.vet[count] != other[count]:
                correspondente = False
                return 0
            count += 1
        return 1


v = cVetor(5)


print(f'Imprimir - Vetor: {v}: ')
print('Tamanho - ', cVetor.tamanho(v))
print('getElemento - ', v[2], '\n')

# setElemento
v[0] = 4
v[1] = 5
v[2] = 7
v[3] = 9
v[4] = 5

print(f'Imprimir - Vetor: {v}: ')
print('Tamanho - ', cVetor.tamanho(v))
print('getElemento - ', v[2], '\n')


print('Minimo - ', cVetor.minimo(v))
print('Maximo - ', cVetor.maximo(v))

#########################################################
u = cVetor(5)

u[0] = 4
u[1] = 5
u[2] = 7
u[3] = 9
u[4] = 5

print(f'\nVetor (U): {u}')

print('E_Identico (v é identico a u?): ', v.eIdentico(u))
#########################################################

#inserir (Aumenta o tamanho do vetor)
cVetor.inserir(v, 8)

print('Vetor: ', v)
print('Inverter - ', cVetor.invert(v))
print('busca(elemento: 5) - ', cVetor.busca(v, 5))
print('ocorrencias(elemento: 5) - ', cVetor.ocorrencias(v, 5))

#remove
cVetor.remove(v, 5)

print('Vetor: ', v, '\n')
print('Média: {}   /   Desvio padrão: {:.2f}'.format(v.gerarEstatisticas()[0], v.gerarEstatisticas()[1]))




